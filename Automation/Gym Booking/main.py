from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
import dotenv
import time

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

try:
    login_button=wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()
except:
    print("Login button click failed")
else:
    print("Login button click succeeded")

try:
    email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(username)
    password_input = driver.find_element(By.ID, "password-input")
    password_input.clear()
    password_input.send_keys(password)
    submit_btn = driver.find_element(By.ID, "submit-button")
    submit_btn.click()
except:
    print("Login failed")
else:
    print("Login succeeded")


wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

booked_count = 0
waitlist_count = 0
already_booked_count = 0

cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
for card in cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text
    if "Tue" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            if button.text == "Booked":
                print(f"✓ Already booked: {class_name} on {day_title}")
                already_booked_count += 1
            elif button.text == "Waitlisted":
                print(f"✓ Already on waitlist: {class_name} on {day_title}")
                already_booked_count += 1
            elif button.text == "Book Class":
                button.click()
                print(f"✓ Successfully booked: {class_name} on {day_title}")
                booked_count +=1
            elif button.text == "Join Waitlist":
                button.click()
                print(f"✓ Joined waitlist for: {class_name} on {day_title}")
                waitlist_count += 1
                time.sleep(1)
            break

print(f"""
------BOOKING SUMMARY------
Classes Booked : {booked_count}
Waitlists Joined : {waitlist_count}
Already Booked/Waitlisted : {already_booked_count}
Total Tuesday 6 PM Classes Processed : {booked_count + waitlist_count + already_booked_count}
""")

