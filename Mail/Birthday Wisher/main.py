import os

from dotenv import load_dotenv
import smtplib

load_dotenv()

sender = os.getenv("SENDER_EMAIL")
password = os.getenv("PASSWORD")
receiver = os.getenv("RECEIVER_EMAIL")


# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="shubhmittal125@hotmail.com",
#         msg="Subject:Hello\n\nBody of email"
#     )