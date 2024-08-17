from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "Laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=3A0IRVO5U3IAW&sprefix=laptop%2Caps%2C253&ref=nb_sb_noss_1")

elam = driver.find_element(By.CLASS_NAME,"puis-card-container")
print(elam.text)

print(elam.get_attribute("outerHTML"),"\n")

time.sleep(5)

driver.close()