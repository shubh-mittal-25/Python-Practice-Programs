import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

load_dotenv()
EMAIL = str(os.getenv("Y_EMAIL"))
PASSWORD = str(os.getenv("Y_PASSWORD"))
UPLOAD_SPEED = 100
DOWNLOAD_SPEED = 100
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach" , True)

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.upload_speed = 0
        self.download_speed = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(2)
        accept_btn = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_btn.click()
        sleep(2)
        btn = self.driver.find_element(By.CLASS_NAME, "start-text")
        btn.click()
        sleep(60)
        self.download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

    def tweet_at_provider(self):
        pass

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()