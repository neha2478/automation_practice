#here we will Learn How to use the chrome Options as arg of Chrome()...in driver.

from selenium import webdriver
from selenium.webdriver import ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized') #start maximized windows
chrome_options.add_argument('headless') #headless
chrome_options.add_argument('--ignore-certificate-errors')#advanced option or certificate error

#here we are using Chrome() but 
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://rahulshettyacademy.com/angularpractice/')
print(driver.title)
print(driver.current_url)

driver.close()