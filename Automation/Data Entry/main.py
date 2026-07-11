import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests

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
print(all_link_elements)

all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
print(all_address_elements)

all_price_elements = soup.select(".PropertyCardWrapper span")
print(all_price_elements)