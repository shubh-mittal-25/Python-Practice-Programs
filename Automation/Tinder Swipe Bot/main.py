import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
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

driver.switch_to.window(base_window)
print(f"Switched to {driver.title}")

sleep(2)
allow_btn = driver.find_element(By.XPATH, "/html/body/main/div/div/form/button")
allow_btn.click()
sleep(2)
not_interested = driver.find_element(By.XPATH, "/html/body/main/div/div/form/button[2]")
not_interested.click()
sleep(2)
accept_btn = driver.find_element(By.XPATH, "/html/body/main/div/div/form/button")
accept_btn.click()

swipes = 0
while swipes < 20:
    sleep(1)
    try:
        like_btn = driver.find_element(By.XPATH, '//*[@id="like-button-container"]/form/button')
        like_btn.click()
        swipes += 1
        print(f"Swiped {swipes} times")
    except ElementClickInterceptedException:
        try:
            driver.find_element(By.CSS_SELECTOR, value='.match-popup a').click()
        except NoSuchElementException:
            pass
    except NoSuchElementException:
        sleep(2)

