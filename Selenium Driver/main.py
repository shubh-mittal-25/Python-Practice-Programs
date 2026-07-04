from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep Chrome Browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach" , True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/Native-M2-Pro-Dispensing-Mineraliser/dp/B0G4CHKBGP/?_encoding=UTF8&ref_=pd_hp_d_btf_homenKitchen")

price = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
print(price)

# driver.close()
driver.quit()