#here we will understand the use of CSS Selectors and other Locators 
'''
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

#To open the Login page 
driver.get("http://127.0.0.1:5000/index.html")

driver.maximize_window() #To maximize the windows 

#Enter Email
driver.find_element(By.ID, "email").send_keys("shruti.karmakr18@gmail.com")

#Enter Password
driver.find_element(By.ID, "password").send_keys("Babai@#Eva2025")

#Click Login Button
driver.find_element(By.TAG_NAME, "button").click()


#Verify Login Success
#driver.current.url - To check the current Url
if "Login.html" in driver.current_url:
    print("Login Successfully")
else:
    print("login Failed!!")

time.sleep(3)

#Close browser
driver.close()
'''
#Another code Example that I Learned here...
#Udemy ...
''''''
from selenium import webdriver

#chrome driver 
from selenium.webdriver.chrome.service import Service 

#--Chrome
from selenium.webdriver.common.by import By

#--time
import time

#Manully importing the Chrome Webdriver
# service_obj = Service("C:\WebDrivers")
# driver = webdriver.Chrome(service = service_obj)

#using Chrome()
driver = webdriver.Chrome()
driver.maximize_window() #It will maximize window
print(driver.title) #tell the title of page
print(driver.current_url) #tells current URL

driver.get("https://rahulshettyacademy.com/client")

#Forgot Link 
#This is LINK_TEXT - from the Link text ...(completely)
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

#here using SH Selector - XPATH - //form/div[1]/input 
#here we will open the page and put inspect , SelectorHub
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")

#Ussing CSS Selector 
#How to write the CSS-Selectors :- here dont write slash
# form div:nth-child(2) input - form to div than nth child 2 (means div 2) inside input
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@123")

#using ID CSS-SELECTOR
#if we use ID than , normal value we can write 
#If we use CSS-SELECTOR, #confirmPassword 
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@123")

#Click on Button
# driver.find_element(By.XPATH,"//button[@type='submit']").click() #checking with Xpath
# driver.find_element(By.TAG_NAME, "button").click() #checking with Tagname
#//button[text() = 'Save new Password'] it will check with text...
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()

print("Task is Successfully Done")

time.sleep(10)

driver.quit()