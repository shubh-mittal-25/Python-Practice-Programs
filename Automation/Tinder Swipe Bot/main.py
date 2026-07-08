import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

load_dotenv()
username = str(os.getenv("TINDOG_USERNAME"))
password = str(os.getenv("PASSWORD"))
url = str(os.getenv("TINDOG_URL"))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
print(f"Currently on {driver.title}")

sleep(2)
login_button = driver.find_element(By.XPATH, "/html/body/header/button")
login_button.click()
sleep(1)
facebook = driver.find_element(By.XPATH, '//*[@id="login-modal"]/div/div/div/button[1]')
facebook.click()

base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
print(f"Switched to {driver.title}")
email_field = driver.find_element(By.ID, "email")
email_field.send_keys(username)
password_field = driver.find_element(By.ID, "pass")
password_field.send_keys(password)
fb_login_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/form/button")
fb_login_btn.click()

sleep(2)
driver.switch_to.window(base_window)
print(f"Switched to {driver.title}")