# NFL Analytis Repository

## Files in Repository
* NFL Se Scraping.ipynb
  * This file was created to scrape data from the web using the Python Selenium. Initially, I used BeautifulSoup; however, I ran into issues with request being denied beause it assumed I was a bot.
  * Using Selenium allowed me to scrape the data I need without running into the issue of bot detection.
* NFL Parsing HTML.ipynb
  * This file goes through the webpages downloaded as HTML files, gets the data that I need, and saves the tables (or data frames) as CSV files.
* Function Writing.py
* Data Cleaning.ipynb
* Basic Analysis.ipynb

## Task List
- [x] Scraping Data from Internet
- [ ] Cleaning Data Prior to Analysis
- [ ] Basic Statistical Analysis
- [ ] Data Visualizations
- [ ] Machine Learning & Deep Learning
- [ ] Interactive Dashboard Using Shiny Apps

## Task By File in Repository
### Data Cleaning
Data To Be Cleaned
- [x] Team Stats
- [ ] Player Offense (**in progress**)
  - [x] Running Backs
  - [x] Quarter Backs
  - [ ] Wide Receivers (Including Tight Ends)
- [ ] Player Defense
- [ ] Advanced Metrics
  - [ ] Defense
  - [ ] Passing
  - [ ] Rushing

## Current Issues
* Going through the team level data, I found some inconsistencies from the 2025 NFL season. I'm not sure why that is, I may rescrape the data as I'm not sure exactly when I did it. I may have do ne it mid season and forgotten to scrape the latter half. The other years don't appear to be having that issue; therefore, I can narrow it down to inconsistencies in scraping data for that specific year. Which is probably a result of inconsistent code or methodologies.