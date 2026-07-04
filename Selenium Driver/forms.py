from selenium import webdriver
from selenium.webdriver.common.by import By

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email = input("Enter your email: ")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach" , True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys(first_name)
l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys(last_name)
e_mail = driver.find_element(By.NAME, "email")
e_mail.send_keys(email)
submit = driver.find_element(By.CSS_SELECTOR, "button")
submit.click()
