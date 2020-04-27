import os
from calendar import weekday, monthrange, SATURDAY

#dependencies from pip
import requests
from PyPDF2 import PdfFileMerger

#-----------
#Change these values to...
SCRAPE_YEAR = 1890 #Select the year you wish to scrape. 1923 and before is public domain.
MAX_PAGES = 99999 #Set to 1000+ to ignore. After it ingests this many pages, it will output "--PARTIAL" file and move on. The average varies, but 35 is a good number for earlier issues; 45 for later issues. The max I've seen was >500, which seemed like a book list.
#------------

def make_url(year, month, day, page_number):
    year = str(year)
    month = str(month).zfill(2)
    day = str(day).zfill(2)
    
    return 'https://archive.publishersweekly.com/?a=is&oid=BG{}{}{}.1.{}&type=pagepdf'.format(year,month,day,page_number)

def download(year, month, day):
    page_number = 1
    merger = PdfFileMerger()
    iso_date = f'{year}-{month:02d}-{day:02d}'

    #Exit early if Issue already downloaded
    if os.path.isfile(f'{iso_date}.pdf'):
        print(iso_date, 'ISSUE ALREADY DOWNLOADED')
        return
    
    print(iso_date, 'BEGIN')
    while True:
        filename = f'{iso_date}--{page_number}.pdf'
        
        #Move to next page if page already downloaded
        if os.path.isfile(filename):
            merger.append(filename) #add page to merger
            print(iso_date, page_number, 'PAGE ALREADY DOWNLOADED')
            page_number+=1
            continue
        
        url = make_url(year, month, day, page_number)
        with requests.get(url) as r:

            if 'Invalid value' in r.text: #page does not exist, output to one pdf
                if page_number == 1:
                    print(f'{iso_date} NO ISSUE FOR THIS DATE\nNEXT\n\n')
                    return
                else:
                    print(f'{iso_date} MERGING...')
                    break

            if page_number > MAX_PAGES:
                print(f'{iso_date} PARTIAL MERGING...')
                break

            with open(filename, 'wb') as f:
                f.write(r.content)  #output individual page PDF
            merger.append(filename) #add page to merger

        print(iso_date, page_number)
        page_number+=1

    #Output
    if page_number <= MAX_PAGES:
        merger.write(f'{iso_date}.pdf') #entire pdf
        merger.close()
        print(f'{iso_date} COMPLETE.')

        #Delete temp files because you have the full file downloaded.
        for i in range(1, page_number):
            os.remove(f'{iso_date}--{i}.pdf')
        print(f'{iso_date} DELETED INDIVIDUAL PAGE PDFS')
    else:
        merger.write(f'{iso_date}--PARTIAL.pdf') #pdf was too long. output partial
        merger.close()
        print(f'{iso_date} PARTIAL COMPLETE.')
    
    print('NEXT\n\n')

def get_issue_dates():
    issue_dates = [] #Tuples of (year, month, day)
    for month in range(1, 13):
        issue_dates.extend([(SCRAPE_YEAR, month, day+1) for day in range(*monthrange(SCRAPE_YEAR, month)) if weekday(SCRAPE_YEAR, month, day+1)==SATURDAY])
    return issue_dates

def main():
    issues = get_issue_dates()
    print(f'DOWNLOADING: {issues}')
    for issue in issues:
        download(*issue)

    print(f'FINISHED {SCRAPE_YEAR}')
    print('CONGRATULATIONS.')

main()
