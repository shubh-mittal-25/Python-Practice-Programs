import os
from dotenv import load_dotenv
import smtplib
import datetime as dt
import random
import requests

MY_LAT = 28.350215
MY_LONG = 79.423187

load_dotenv()

sender = os.getenv("SENDER_EMAIL")
password = os.getenv("PASSWORD")
receiver = os.getenv("RECEIVER_EMAIL")

now = dt.datetime.now()
day_hour = now.hour

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted":0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json" , params=parameters)
response.raise_for_status()
data = response.json()
sunrise_time = data["results"]["sunrise"]
sunset_time = data["results"]["sunset"]

with open("Mail/Quote of the day/quotes.txt") as file:
    quotes = file.readlines()
today_quote = random.choice(quotes)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=sender, password=password)
    connection.sendmail(
        from_addr=sender,
        to_addrs=sender,
        msg=f"Subject:Motivational Quote of the day\n\n{today_quote}"
    )

