import os
import smtplib
import random
import datetime
import requests

MY_LAT = 28.350215
MY_LONG = 79.423187

sender = os.environ["SENDER_EMAIL"]
password = os.environ["PASSWORD"]
receiver = os.environ["RECEIVER_EMAIL"]

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

with open("quotes.txt") as file:
    quotes = file.readlines()
today_quote = random.choice(quotes)

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=sender, password=password)
    connection.sendmail(
        from_addr=sender,
        to_addrs=sender,
        msg=f"Subject:Motivational Quote of the day\n\n{today_quote}\n\nSunrise Time : {sunrise_time}\nSunset Time : {sunset_time}"
    )