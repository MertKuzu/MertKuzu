#This app is sign in account, getting follower and showing it and save



from selenium.webdriver.common import keys
from instaUserInfo import username, password      #I'm using my account info here with another .py file
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(3)
        #self.browser.fullscreen_window()
        #time.sleep(3)
        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(self.username)
        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(self.password)
        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").send_keys(Keys.ENTER)
        time.sleep(3)
        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").send_keys(Keys.ENTER)
        time.sleep(3)
        #self.browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").send_keys(Keys.ENTER)


    #this is getting follower list 
    def getFollower(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(3)
        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(3)
        dialog = self.browser.find_element_by_css_selector(".jSC57._6xe7A")
        time.sleep(3)
        followerCount = len(dialog.find_elements_by_css_selector("li"))
        print(f"first count: {followerCount}")

        action = webdriver.ActionChains(self.browser)    

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()   
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(5)

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if newCount != followerCount:
                followerCount = newCount
                print(f"Updated count: {newCount}")
                time.sleep(5)
            else:
                break

        followerList = []            
        followers = dialog.find_elements_by_css_selector("li")
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            followerList.append(link)

        with open("follower.txt","w", encoding="utf-8") as file:
            for item in followerList:
                file.write(item+"\n")
        

insta = Instagram(username,password)

insta.signIn()
insta.getFollower()