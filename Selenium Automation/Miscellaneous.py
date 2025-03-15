#What is JS executor?,
# here we will Learn how wecan execute Javascript using Selenium
# Js events we can execute in our Selenium tests.

#Executing Js using Selenium 

#window.scrollBy(0, document.body.scrollHeight) - JS example

#in Inspect we can go to consol in Inspect and execute JS

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#headless - backend everything we be done.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('---ignore-certifcate-error-')
#for this we need to manually add Location of exe file
# service_obj = Service('C:\WebDrivers')
# driver = webdriver.Chrome(service=service_obj, option=chrome_Options)

#here my driver was not manually loaded so i am using this way.
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(2)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

#driver.execute_script() - here it will execute Javascript in it.
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

#To take screenshot as file - of errors
# get_screenshot_as_file('name of file.'), we can use samilar moe functions 
driver.get_screenshot_as_file('ss1.png') #it will tatakescrrenshort

print('Task Done hooray!!')