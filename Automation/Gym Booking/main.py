from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
import dotenv

loaded = dotenv.load_dotenv()
gym_url = str(os.getenv("URL"))
username = str(os.getenv("GYM_USER"))
password = str(os.getenv("PASSWORD"))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach" , True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(gym_url)

wait = WebDriverWait(driver, 2)

login_button=wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
email_input.clear()
email_input.send_keys(username)
password_input = driver.find_element(By.ID, "password-input")
password_input.clear()
password_input.send_keys(password)

submit_btn = driver.find_element(By.ID, "submit-button")
submit_btn.click()

wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))