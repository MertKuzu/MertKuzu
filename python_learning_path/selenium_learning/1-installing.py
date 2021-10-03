#Selenium learning


from selenium import webdriver

driver = webdriver.Firefox()
driver2= webdriver.Chrome()

url = "https://www.youtube.com"

driver.get(url)
driver2.get(url)