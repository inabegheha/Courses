# -------------------------------------------- #

# Driver Google Chrome Bayad Download Shavad
# Baraye Chrome : chromedriver.exe 
# Site For Download Selenium Drivers : 
# https://selenium-python.readthedocs.io/

# -------------------------------------------- #

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username_textbox_id = 'txtUsername'
        self.password_textbox_id = 'txtPassword'
        self.login_button_id = 'btnLogin'

    def EnterUsername(self,username):
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def EnterPassword(self,password):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element_by_id(self.login_button_id).click()

