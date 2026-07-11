import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

load_dotenv()
form_url = str(os.getenv("FORM_URL"))
zillow_url = str(os.getenv("ZILLOW_URL"))

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(zillow_url, headers=header)
data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = []
for link in all_link_elements:
    all_links.append(link["href"])
print(len(all_links))
print(all_links)
print("\n-----------------------------------------------------------\n")

all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_address = []
for address in all_address_elements:
    add = address.getText()
    add = add.strip()
    add = add.replace(" | ", " ")
    all_address.append(add)
print(len(all_address))
print(all_address)
print("\n-----------------------------------------------------------\n")

all_price_elements = soup.select(".PropertyCardWrapper span")
all_price = []
for price in all_price_elements:
    p = price.getText()
    p = p.replace("/mo", "").split("+")[0]
    all_price.append(p)
print(len(all_price))
print(all_price)
print("\n-----------------------------------------------------------\n")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(form_url)