import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

load_dotenv()
username = str(os.getenv("SAN_EMAIL"))
password = str(os.getenv("SAN_PASSWORD"))
SIMILAR_ACCOUNT = ("chefsteps")
URL = "https://app.100daysofpython.dev/services/share-a-naan/login"

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(URL)
        sleep(2)
        username_field = self.driver.find_element(By.ID, "username")
        username_field.send_keys(username)
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        login_btn = self.driver.find_element(By.CLASS_NAME, "naan-btn-primary")
        login_btn.click()
        sleep(2)

        save_info = self.driver.find_elements(By.XPATH, "//div[contains(text(), 'Not now')]")
        if save_info:
            save_info[0].click()
        sleep(1)

        notifications = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Not Now')]")
        if notifications:
            notifications[0].click()

    def find_followers(self):
        pass

    def follow(self):
        pass

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()