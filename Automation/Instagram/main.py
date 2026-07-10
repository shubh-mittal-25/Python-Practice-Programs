import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()
username = str(os.getenv("SAN_EMAIL"))
password = str(os.getenv("SAN_PASSWORD"))
SIMILAR_ACCOUNT = ("chefsteps")
URL = "https://app.100daysofpython.dev/services/share-a-naan"
LOGIN_URL = f"{URL}/login"

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()