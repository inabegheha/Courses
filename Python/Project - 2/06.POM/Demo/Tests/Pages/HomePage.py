# -------------------------------------------- #

# Driver Google Chrome Bayad Download Shavad
# Baraye Chrome : chromedriver.exe 
# Site For Download Selenium Drivers : 
# https://selenium-python.readthedocs.io/

# -------------------------------------------- #

class HomePage:
    def __init__(self,driver):
        self.driver = driver
        self.welcome_link_id = 'welcome'
        self.logout_link_linktext = 'Logout'

    def ClickWelcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def ClickLogout(self):
        self.driver.find_element_by_link_text(self.logout_link_linktext).click()
    