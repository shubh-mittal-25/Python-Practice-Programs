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

for n in range(len(all_links)):
    driver.get(form_url)
    time.sleep(2)

    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(all_address[n])
    price.send_keys(all_price[n])
    link.send_keys(all_links[n])
    submit_btn.click()