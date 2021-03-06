# publishers-weekly-archive
Scripts for scraping PDFs off the *Publishers Weekly* archive site.

Requirements: Python 3.7+, [requests](https://2.python-requests.org/en/master/), [PyPDF2](https://pythonhosted.org/PyPDF2/). (Python 3.6 should also work because the most advanced feature is f-strings.)

They use global variables for configuration.

## publishers-weekly-year.py
Download an entire year of issues.
* `SCRAPE_YEAR`: Target the year that you want to download.
* `MAX_PAGES`: If your connection is fine and you're only interested in downloading complete PDFs, set this to a high number and ignore it. The number of pages from the beginning you want to download; the script outputs a file marked "--PARTIAL."

## publishers-weekly-single.py
Download an issue on a particular day. Mostly for downloading the volume indexes or filling in "PARTIAL" PDFs later.
* `SCRAPE_YEAR`, `SCRAPE_MONTH`, `SCRAPE_DAY`: Target the date that you want to download.
* `MAX_PAGES`: If your connection is fine and you're only interested in downloading complete PDFs, set this to a high number and ignore it. The number of pages from the beginning you want to download.
