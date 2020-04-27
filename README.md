# publishers-weekly-archive
Scripts for scraping PDFs off the Publishers Weekly archive site.

They use global variables for configuration.

## publishers-weekly-year.py
`SCRAPE_YEAR`: Target the year that you want to download.
`MAX_PAGES`: Don't worry about this if your connection is fine. The number of pages from the beginning you want to download. Set to a high number to ignore.

## publishers-weekly-single.py
`SCRAPE_YEAR`, `SCRAPE_MONTH`, `SCRAPE_DAY`: Target the date that you want to download].
`MAX_PAGES`: Don't worry about this if your connection is fine. The number of pages from the beginning you want to download. Set to a high number to ignore.
