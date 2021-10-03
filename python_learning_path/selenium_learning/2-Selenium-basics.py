#I'm trying to some selenium command

from selenium import webdriver
import time

driver = webdriver.Firefox()

url = "https://github.com"

driver.get(url)

time.sleep(3)
print(driver.title)
time.sleep(3)
driver.maximize_window()
# driver.save_screenshot("github.com-homepage.png")
time.sleep(3)
url = "https://github.com/MertKuzu"
driver.get(url)

print(driver.title)

if "MertKuzu" in driver.title:
    driver.save_screenshot("github-mertkuzu.png")

time.sleep(3)
driver.back()
time.sleep(3)
driver.close()