#  Remote Job Scraper

A web scraper that extracts remote developer job listings from [We Work Remotely](https://weworkremotely.com/) and saves them to a structured CSV file for analysis or visualization.

---

##  Project Overview

-  **Source**: We Work Remotely – Remote Programming Jobs  
-  **Tools**: `requests`, `BeautifulSoup`, `pandas`, `lxml`  
-  **Output**: CSV file containing job titles, companies, locations, and links  

---

##  Features

- Scrapes live job postings from We Work Remotely
- Extracts title, company, region, and job URL
- Saves results into `data/wwr_remote_jobs.csv`
- Uses `lxml` parser for faster and cleaner HTML parsing
