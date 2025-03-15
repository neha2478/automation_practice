#Handling Java/JS pop up using Selenium 

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
'''
Enter on text box Switch to Alert Example which
Inspect that 
'''
driver.find_element(By.CSS_SELECTOR, "#name").send_keys('Shruti') #here we can use id , class..

time.sleep(2)

driver.find_element(By.ID, "alertbtn").click() #here it will click on alert 
alert = driver.switch_to.alert #here it will only consider Alert msg
alertText = alert.text #text- wll fetch the text

time.sleep(2)

assert 'Shruti' in alertText # will check weather Shruti is there in assert or not

print(alertText)
#to click on Ok button
alert.accept() #To ok
# alert.dismiss() #to cancle

time.sleep(3)
driver.quit()