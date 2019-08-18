# NABEGHEHA.COM

# -------------------------------------------- #

# Driver Google Chrome Bayad Download Shavad
# Baraye Chrome : chromedriver.exe 
# Site For Download Selenium Drivers : 
# https://selenium-python.readthedocs.io/

# -------------------------------------------- #

from selenium import webdriver
import time

driver = webdriver.Chrome(r'..\Driver\chromedriver.exe')

driver.get('https://opensource-demo.orangehrmlive.com/')

driver.find_element_by_id('txtUsername').send_keys('Admin')
driver.find_element_by_id('txtPassword').send_keys('admin123')
time.sleep(4)

driver.find_element_by_id('btnLogin').click()
time.sleep(4)

driver.find_element_by_id('welcome').click()
time.sleep(4)
driver.find_element_by_link_text('Logout').click()


driver.close()
driver.quit()