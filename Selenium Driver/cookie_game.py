from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach" , True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

sleep(3)
print("Looking for language selection...")
try:
    lang_button = driver.find_element(by=By.ID, value="langSelect-EN")
    print("Found language button, clicking...")
    lang_button.click()
    sleep(3) # more loading
except NoSuchElementException:
    print("Language selection not found")
sleep(2)

cookie = driver.find_element(By.ID, "bigCookie")
store_items = [f"product{i}" for i in range(18)]

wait_time = 5
timeout = time() + wait_time  # Check for purchases every 5 seconds

while True:
    cookie.click()
    if time() > timeout:
        try:
            cookies_count = int(driver.find_element(by=By.ID, value="cookies").text.split()[0].replace(",", ""))
            # Find all available products in the store
            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")
            # Find the most expensive item we can afford
            best_item = None
            for product in reversed(products):  # Start from most expensive (bottom of list)
                # Check if item is available and affordable (enabled class)
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break
            # Buy the best item if found
            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or items")

            # Reset timer
        timeout = time() + wait_time




