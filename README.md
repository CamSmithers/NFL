# NFL Analytis Repository

## Files in Repository
* NFL Se Scraping.ipynb
  * This file was created to scrape data from the web using the Python Selenium. Initially, I used BeautifulSoup; however, I ran into issues with request being denied beause it assumed I was a bot.
  * Using Selenium allowed me to scrape the data I need without running into the issue of bot detection.
* NFL Parsing HTML.ipynb
  * This file goes through the webpages downloaded as HTML files, gets the data that I need, and saves the tables (or data frames) as CSV files.
* Function Writing.py
  * This file will hold custom functions that I may create. Not sure if I'll make any or those in pandas and numpy will suffice.
* Data Cleaning.ipynb
  * This file is for all of the basic data cleaning that I will needed. Essentially, cleaning up variable names, filtering rows, creating some aggregregates.
* Basic Analysis.ipynb
  * This file is for basic statistical analysis and visualizations. More along the line of descriptive statistics; juxtapose, inferential statistics.

## Task List
- [x] Scraping Data from Internet
- [x] Cleaning Data Prior to Analysis
- [x] Basic Analysis & Visualizations
- [ ] Machine Learning & Deep Learning
- [ ] Dashboard

## Task By File in Repository

### Data Cleaning
Data To Be Cleaned
- [x] Team Stats
- [x] Player Offense 
  - [x] Running Backs
  - [x] Quarter Backs
  - [x] Wide Receivers (Including Tight Ends)
- [x] Advanced Metrics
  - [x] Defense
  - [x] Passing
  - [x] Rushing

### Basic Analysis
- [x] Summary Statistics
- [x] Data Tables
- [ ] Various Plots
  - [x] Boxplots
  - [x] Histograms
  - [x] Scatterplots
  - [x] Advanced Plots (Hybrid Plots)