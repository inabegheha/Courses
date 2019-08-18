# NABEGHEHA.COM

# Driver Google Chrome Bayad Download Shavad
# Baraye Chrome : chromedriver.exe 
# Site For Download Selenium Drivers : 
# https://selenium-python.readthedocs.io/


from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://google.com')
driver.find_element_by_name('q').send_keys('سایت آموزشی نابغه ها')
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[3]/center/input[1]').send_keys(Keys.ENTER)
driver.execute_script("window.scrollTo(0, 300)") 
time.sleep(3)
driver.execute_script("window.scrollTo(0, 500)") 
time.sleep(3)
driver.execute_script("window.scrollTo(0, 100)") 
time.sleep(3)
driver.execute_script("window.scrollTo(0, 400)") 

time.sleep(30)
driver.quit()

