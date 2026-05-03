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
### General
- [ ] Scrape data for the 2025 NFL season.

### Data Cleaning
Data To Be Cleaned
- [x] Team Stats
- [x] Player Offense 
  - [x] Running Backs
  - [x] Quarter Backs
  - [x] Wide Receivers (Including Tight Ends)
- [ ] ~~Player Defense~~
- [x] Advanced Metrics
  - [x] Defense
  - [x] Passing
  - [x] Rushing

## Current Issues
* Going through the team level data, I found some inconsistencies from the 2025 NFL season. I'm not sure why that is, I may rescrape the data as I'm not sure exactly when I did it. I may have do ne it mid season and forgotten to scrape the latter half. The other years don't appear to be having that issue; therefore, I can narrow it down to inconsistencies in parsing data for that specific year. Which is probably a result of inconsistent code or methodologies.
  * I have realised that the issues stems from how I was grouping the years. In other projects I have a variable that contains the season (year) as a variable; however, I used the year from the `gamedate` variable for my season (year) variable. This causes an issue because the season starts in one year and finishes in the next. For example the 2024 NFL season has the regular season all in 2024 and post season in 2025.
  * This nails down my issue to not scraping the 2025 NFL season, the 2025 dates are from the 2024 season's playoff games.
  * I'll either have to create a specific season variable for each table parse from the HTML files or create a conditional variable that sets the year based on a range of dates.