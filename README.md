# Google Company Summary Scraper

This project is a Python-based web scraper that automates the process of fetching company summaries from Google Search. It reads a list of company names from an input CSV file and outputs a new CSV file containing the scraped summaries.

## Features
- Reads company names from `companies.csv`.
- Uses Selenium WebDriver to search Google for `{Company Name} company`.
- Automatically handles Google's CAPTCHA by pausing the script and waiting for manual verification.
- Cleans the scraped text to remove unnecessary artifacts.
- Saves the extracted summaries to `company_summaries.csv`.

## Prerequisites
- Python 3.x
- Google Chrome browser

## Dependencies
Install the required Python packages using pip:
```bash
pip install selenium webdriver-manager pandas
```

## Usage

1. Ensure you have a `companies.csv` file in the project directory. The company names should be listed in the first column.
2. Run the scraper script:
   ```bash
   python fetch_summary.py
   ```
3. The script will open a Chrome browser window and begin fetching summaries. 
   - **Note on CAPTCHAs:** If Google detects automated queries and presents a CAPTCHA, the script will pause. You must solve the CAPTCHA manually in the opened Chrome window. Once solved, the script will automatically resume.
4. Once finished, the results will be saved in `company_summaries.csv`.

## Project Structure
- `fetch_summary.py`: The main scraping script.
- `companies.csv`: The input CSV file containing company names.
- `company_summaries.csv`: The output CSV file containing the scraped summaries.

## Author
- **Rohit Kadian**
