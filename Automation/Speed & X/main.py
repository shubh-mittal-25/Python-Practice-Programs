import os
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()
EMAIL = str(os.getenv("Y_EMAIL"))
PASSWORD = str(os.getenv("Y_PASSWORD"))
UPLOAD_SPEED = 100
DOWNLOAD_SPEED = 100

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.upload_speed = 0
        self.download_speed = 0

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()