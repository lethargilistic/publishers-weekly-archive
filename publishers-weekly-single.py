import os

#pip dependencies
import requests
from PyPDF2 import PdfFileMerger

#-----------
#Change these values to...
SCRAPE_YEAR = 1892 #Select the year you wish to scrape. 1923 and before is public domain.
SCRAPE_MONTH = 1
SCRAPE_DAY= 30
MAX_PAGES = 99999 #After it ingests this many pages, it will output "--PARTIAL" file and move on. The average is ~24. The max I've seen is 156, which seemed like a book list. Just set to 1000+ to ignore this.
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
        merger.append(filename) #add page to merger
        print(iso_date, 'ISSUE ALREADY DOWNLOADED')
        return
        
    print(iso_date, 'BEGIN')
    while True:
        filename = f'{iso_date}--{page_number}.pdf'
        
        #Move to next page if page already downloaded
        if os.path.isfile(filename):
            print(iso_date, page_number, 'PAGE ALREADY DOWNLOADED')
            page_number+=1
            continue
        
        url = make_url(year, month, day, page_number)
        r = requests.get(url)

        if 'Invalid value' in r.text: #page does not exist, output to one pdf
            print(f'{iso_date} MERGING...')
            break

        if page_number > MAX_PAGES:
            print('{iso_date} PARTIAL MERGING...')
            break
        
        with open(filename, 'wb') as f:
            f.write(r.content)  #output page just in case
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

def main():
    print(f'INDIVIDUAL YEAR SCRAPE')
    
    download(SCRAPE_YEAR, SCRAPE_MONTH, SCRAPE_DAY)

    print(f'CONGRATULATIONS.')

main()
