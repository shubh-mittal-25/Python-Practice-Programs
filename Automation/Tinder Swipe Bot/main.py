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

