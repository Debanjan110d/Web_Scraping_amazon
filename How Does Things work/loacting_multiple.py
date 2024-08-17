from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "Laptop"
for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=3A0IRVO5U3IAW&sprefix=laptop%2Caps%2C253&ref=nb_sb_noss_1")

    elems = driver.find_elements(By.CLASS_NAME,"puis-card-container")
    print(f"{len(elems)} is found ")
    for elem in elems:
        print(elem.text)


    time.sleep(5)

    driver.close()