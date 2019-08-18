# NABEGHEHA.COM

# Driver Google Chrome Bayad Download Shavad
# Baraye Chrome : chromedriver.exe 
# Site For Download Selenium Drivers : 
# https://selenium-python.readthedocs.io/

#--------------------------------------------

# Address e instabot : 
# https://github.com/instabot-py/instabot.py

#--------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def CloseBrowser(self):
        self.driver.close()   

    def Login(self):
        driver = self.driver 
        driver.get('https://www.instagram.com/')  
        time.sleep(2)    
        login_button = driver.find_element_by_xpath('//a[@href="/accounts/login/?source=auth_switcher"]')
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.ENTER)
        time.sleep(1)
        driver.get("https://www.instagram.com/YourUserName/")


    def like_photo(self,hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(2)
        pic_hrefs = []
        for i in range(1,2):

            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(2)
                # Bedast Avardan Hameye Element Hayi k Tag ((a)) Hastan
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # Joda Kardan Link Aks Ha Az Baghie Link Ha
                pic_hrefs = [elem.get_attribute('href') for elem in hrefs_in_view if '.com/p/' in elem.get_attribute('href')]

            except Exception:
                continue    

        # Code For Liking photos
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)

            try:
                time.sleep(random.randint(1,2))
                driver.find_element_by_xpath('//span[@aria-label="Like"]').click()

            except Exception as e :
                time.sleep(2)    


# ---------------------- #
username = "YourUserName"
password = "YourPassword"
# ---------------------- #

ig = InstagramBot(username,password)
ig.Login()
hashtag = ['animals']

while True:
    try:
        
        tag = random.choice(hashtag)
        ig.like_photo(tag)

    except Exception:
        ig.CloseBrowser()
        time.sleep(50)
        ig = InstagramBot(username,password)
        ig.Login()    