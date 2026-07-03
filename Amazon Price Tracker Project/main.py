from bs4 import BeautifulSoup
import requests
import os
import dotenv
import smtplib

BUY_PRICE = 100
dotenv.load_dotenv()
sender = os.getenv("SENDER_EMAIL")
password = os.getenv("PASSWORD")

response = requests.get("https://appbrewery.github.io/instant_pot/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
price = float(f"{soup.find("span", class_="a-price-whole").getText()}{soup.find("span", class_="a-price-fraction").getText()}")
title = soup.find(id="productTitle").get_text().strip()


if price < BUY_PRICE:
    message = f"{title} is on sale for {price}!"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(
            from_addr=sender,
            to_addrs=sender,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\nURL".encode("utf-8")
        )
