# -------------------------------------------- #

# Driver Google Chrome Bayad Download Shavad
# Baraye Chrome : chromedriver.exe 
# Site For Download Selenium Drivers : 
# https://selenium-python.readthedocs.io/

# -------------------------------------------- #

from selenium import webdriver
import time
import unittest
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r'..\Driver\chromedriver.exe')


    def test_LoginValid(self):

        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        login = LoginPage(driver)
        login.EnterUsername('admin')
        time.sleep(3)
        login.EnterPassword('admin123')
        time.sleep(2)
        login.ClickLogin()

        homepage = HomePage(driver)

        homepage.ClickWelcome()
        time.sleep(2)
        homepage.ClickLogout()
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()  
        
if __name__ == '__main__':
    unittest.main()