#I'm using my information here from diffirent .py file

from githubUserInfo import username, password    
from selenium import webdriver
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Firefox()
        self.username = username
        self.password = password
        self.following = []

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(3)

        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)

        time.sleep(3)

        self.browser.find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[12]").click()

    def getFollowing(self):
        self.browser.get(f"https://github.com/{self.username}?tab=following")
        time.sleep(3)

        items = self.browser.find_elements_by_css_selector(".d-table.table-fixed")

        for i in items:
            self.following.append(i.find_element_by_css_selector(".f4.Link--primary").text)

github = Github(username, password)
github.signIn()
time.sleep(3)
github.getFollowing()
for text in github.following:
    print(text)