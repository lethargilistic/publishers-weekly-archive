# publishers-weekly-archive
Scripts for scraping PDFs off the Publishers Weekly archive site.

They use global variables for configuration.

## publishers-weekly-year.py
Download an entire year of issues.
* `SCRAPE_YEAR`: Target the year that you want to download.
* `MAX_PAGES`: If your connection is fine and you're only interested in downloading complete PDFs, set this to a high number and ignore it. The number of pages from the beginning you want to download; the script outputs a file marked "--PARTIAL."

## publishers-weekly-single.py
Download an issue on a particular day. Mostly for downloading the volume indexes or filling in "PARTIAL" PDFs later.
* `SCRAPE_YEAR`, `SCRAPE_MONTH`, `SCRAPE_DAY`: Target the date that you want to download.
* `MAX_PAGES`: If your connection is fine and you're only interested in downloading complete PDFs, set this to a high number and ignore it. The number of pages from the beginning you want to download.
