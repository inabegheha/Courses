# NABEGHEHA.COM

# Driver Google Chrome Bayad Download Shavad
# Baraye Chrome : chromedriver.exe 
# Site For Download Selenium Drivers : 
# https://selenium-python.readthedocs.io/


from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://web.whatsapp.com/')

# Baraye Daryafte Chand Esm : 
names = input('Enter names with comma (name1,name2,...) : ')
a = names.split(',')
names = list(a)

msg = input('Enter msg : ')
count = int(input('How many times ???  : '))

input('Enter Anything ...')

for name in names:
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    
    # Deghat Konid !!!! Class_name Momkene Taghir Kone !!!!
    msg_box = driver.find_element_by_class_name('_2S1VP')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()