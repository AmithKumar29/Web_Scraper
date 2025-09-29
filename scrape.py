import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching Chrome browser...")
    chrome_driver_path = "C:/Users/amith/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page loaded successfully...")
        html = driver.page_source
        time.sleep(5)  # adjust/remove in production
        return html
    finally:
        driver.quit()


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    return str(body_content) if body_content else "No body content found"


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')
    for script in soup(["script", "style"]):
        script.decompose()
    text = soup.get_text(separator='\n')
    lines = [line.strip() for line in text.splitlines()]
    cleaned_text = '\n'.join(line for line in lines if line)
    return cleaned_text


def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)]
