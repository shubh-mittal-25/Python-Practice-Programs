import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

load_dotenv()
EMAIL = str(os.getenv("Y_EMAIL"))
PASSWORD = str(os.getenv("Y_PASSWORD"))


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.upload_speed = 0
        self.download_speed = 0
        self.UPSPEED = 100
        self.DOWNSPEED = 100

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(2)
        accept_btn = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_btn.click()
        sleep(2)
        btn = self.driver.find_element(By.CLASS_NAME, "start-text")
        btn.click()
        sleep(40)
        self.download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        if int(self.download_speed) < self.DOWNSPEED or int(self.upload_speed) < self.UPSPEED:
            return True
        else:
            return False

    def tweet_at_provider(self):
        self.driver.get("https://app.100daysofpython.dev/services/y")
        sleep(2)
        ok_btn = self.driver.find_element(By.CLASS_NAME, "y-btn-primary")
        ok_btn.click()
        login_btn = self.driver.find_element(By.CLASS_NAME, "y-login-link")
        login_btn.click()
        sleep(2)

        self.driver.find_element(By.NAME, value="email").send_keys(EMAIL)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        sleep(3)
        tweet_compose = self.driver.find_element(By.CSS_SELECTOR, value='div[aria-label="Post text"]')
        tweet = f"Hey Internet Provider, why is my speed {self.download_speed}down/{self.upload_speed}up when I pay for {self.DOWNSPEED}down/{self.UPSPEED}up?!"
        tweet_compose.send_keys(tweet)

        sleep(2)
        tweet_button = self.driver.find_element(By.CSS_SELECTOR, value='.x-compose-form button')
        tweet_button.click()

        sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
internet = bot.get_internet_speed()
if internet:
    bot.tweet_at_provider()