from selenium import webdriver
import os
import dotenv

dotenv.load_dotenv()
gym_url = str(os.getenv("URL"))
username = str(os.getenv("USERNAME"))
password = str(os.getenv("PASSWORD"))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach" , True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(gym_url)
