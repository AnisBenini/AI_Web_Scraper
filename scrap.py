import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import undetected_chromedriver as uc

def scrape_website(website):
    print('Launching Chrome browser...')


    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)



    try:
        driver.get(website)
        print("Page Loaded...")
        html=driver.page_source
        time.sleep(5)
        return html
    
    finally :
        driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script","style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content= "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
                                                            
        )
    
    return cleaned_content

def split_dom_content(dom_content, max_length=7000):
    return [
        dom_content[i : i + max_length] for i in range ( 0, len(dom_content), max_length)
    ]