from bs4 import BeautifulSoup
import requests
import os
import dotenv
import smtplib

BUY_PRICE = 1000
dotenv.load_dotenv()
sender = os.getenv("SENDER_EMAIL")
password = os.getenv("PASSWORD")
url = "https://www.amazon.in/VAYA-Hautechef-Pre-Seasoned-Cast-Kadhai/dp/B0F44BLP6X/?_encoding=UTF8&ref_=pd_hp_d_btf_LPDEALS"
response = requests.get(url)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
price = float(soup.find("span", class_="a-price-whole").getText())
title = soup.find(id="productTitle").get_text().strip()

if price < BUY_PRICE:
    message = f"{title} is on sale for {price}!"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(
            from_addr=sender,
            to_addrs=sender,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
