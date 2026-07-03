from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/instant_pot/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
price = f"{soup.find("span", class_="a-price-whole").getText()}{soup.find("span", class_="a-price-fraction").getText()}"
print(price)