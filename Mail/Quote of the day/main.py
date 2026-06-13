import os
from dotenv import load_dotenv
import smtplib
import datetime as dt
import random

load_dotenv()

sender = os.getenv("SENDER_EMAIL")
password = os.getenv("PASSWORD")
receiver = os.getenv("RECEIVER_EMAIL")

now = dt.datetime.now()
day_hour = now.hour

if day_hour == 8:
    with open("quotes.txt") as file:
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
