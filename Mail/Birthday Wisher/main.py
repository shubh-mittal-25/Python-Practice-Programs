import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

sender = os.getenv("SENDER_EMAIL")
password = os.getenv("PASSWORD")
receiver = os.getenv("RECEIVER_EMAIL")


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=sender, password=password)
    connection.sendmail(
        from_addr=sender,
        to_addrs=receiver,
        msg="Subject:Hello(2)\n\nBody of email"
    )