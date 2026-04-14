from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import re


options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)


def clean_summary(text):
    text = re.split(r'\n[A-Z].*\+\d+', text)[0]
    text = text.replace("\n", " ")
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def wait_if_captcha():
    # only pause if captcha page loaded
    if "sorry" in driver.current_url.lower():
        print("\n⚠️ Google human verification detected")
        print("Solve it manually in Chrome...")
        
        # wait until captcha solved
        while "sorry" in driver.current_url.lower():
            time.sleep(1)

        print("✅ Captcha solved. Continuing...")


def get_summary_from_google(company_name):
    try:
        url = f"https://www.google.com/search?q={company_name}+company"
        driver.get(url)

        wait_if_captcha()

        time.sleep(2)

        elements = driver.find_elements(By.CSS_SELECTOR, "div.Y3BBE")

        for el in elements:
            text = el.text.strip()
            if len(text) > 30:
                return clean_summary(text)

        return "Summary not found"

    except:
        return "Summary not found"


def main():
    df = pd.read_csv("companies.csv")
    df.columns = df.columns.str.strip()

    companies = df.iloc[:, 0].tolist()

    results = []

    for company in companies:
        print("Fetching:", company)

        summary = get_summary_from_google(company)

        results.append({
            "Company Name": company,
            "Summary": summary
        })

        time.sleep(2)

    pd.DataFrame(results).to_csv("company_summaries.csv", index=False)

    print("\nDone")


if __name__ == "__main__":
    try:
        main()
    finally:
        driver.quit()