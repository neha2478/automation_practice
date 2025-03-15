#Write a Selenium code on Complete Web Form

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome()
driver.maximize_window()
print(driver.title)
print(driver.current_url)

#To get the Driver Link
driver.get("https://formy-project.herokuapp.com/form")

#Enter Firstname
driver.find_element(By.ID, "first-name").send_keys("Eva")

#Enter Lastname
driver.find_element(By.ID, "last-name").send_keys("Saha")

#Enter Job Title
driver.find_element(By.ID, "job-title").send_keys('Automation Tester')

#Select the radio Button
driver.find_element(By.ID, "radio-button-2").click()

#Select the Check box 
driver.find_element(By.XPATH, "//input[@value = 'checkbox-2']").click()

# Select an option from the dropdown
dropdown = driver.find_element(By.ID, 'select-menu')
select = Select(dropdown)
select.select_by_visible_text('0-1')

#Another way 
# dropdown = Select(driver.find_element(By.ID, 'select-menu')).select_by_visible_text('0-1')

#select Date
driver.find_element(By.ID, 'datepicker').send_keys('06/03/2025')

#Click on Button 
#for class - CSS-Slector => .class_name
driver.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary').click()
#Another way
# driver.find_element(By.CLASS_NAME, 'btn btn-lg btn-primary').click()

time.sleep(3)

# msg = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success").text #text - will fetch text
#using class_name
msg = driver.find_element(By.CLASS_NAME, "alert").text
print(msg)

time.sleep(2)

# driver.close()
