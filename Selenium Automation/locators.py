#Locators :- ID, Xpath, CSS-Selectors, Classname, name, linkText

#here I am using one demo Test Automation Page .
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

#Open the login page
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

#Enter Username
driver.find_element(By.NAME, "username").send_keys("student")

#Enter password
driver.find_element(By.ID, "password").send_keys("Password123")

# Click the Submit button
driver.find_element(By.ID, "submit").click()

print("✅ Login form submitted successfully!")

#Wait to observe the I/P before closing (optional)
# input('Press Enter to close the browser...') # This keeps the browser open until you press Enter
# print("Logged in Successfully!!")

time.sleep(3)

driver.quit()
'''

# Test case 2: Negative username test
# Open page
# Type username incorrectUser into Username field
# Type password Password123 into Password field
# Push Submit button
# Verify error message is displayed
# Verify error message text is Your username is invalid!

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

print(driver.title)

print(driver.current_url)

#Enter incorrect Username 
driver.find_element(By.NAME, "username").send_keys("incorrectUser")

#Enter incorrect password 
driver.find_element(By.ID, "password").send_keys("Password123")

#Press Submit Button
driver.find_element(By.ID, "submit").click()

#Wait for the error Message
time.sleep(3) # Simple wait (not recommended for real automation)

#Get error message
error_msg = driver.find_element(By.ID, "error").text

print(error_msg)

# assert error_msg == "Your username is invalid!", "Error message is mismatch!" #here we are using the assert to check that 

print("Negative Username Test Password")

#closing the browser
driver.quit()

# O/P :-
'''
Test Login | Practice Test Automation
https://practicetestautomation.com/practice-test-login/
[15412:18148:0304/170411.005:ERROR:page_load_metrics_update_dispatcher.cc(195)] Invalid first_paint 2.189 s for first_meaningful_paint 2.178 s
[15412:18148:0304/170411.141:ERROR:page_load_metrics_update_dispatcher.cc(195)] Invalid first_paint 2.189 s for first_meaningful_paint 2.178 s
Negative Username Test Password
'''

#//tagname[@attribute='value] -> //input
#Press Submit Button
# driver.find_element(By.ID, "submit").click()
#for this if it had type of value as attribute than we had to use xpath
#driver.find_elemnt(By.XPATH, /input[@type= 'submit]/).click() # any way lick this


#Explaination for error msg
# error_msg = driver.find_element(By.ID, "error").text

# where we are fetching the error mssg using find_elemnt() , By .Id, text
#text - fetch the text 
#storing it into the variable 

#CSS - tagename[attribute='value'] -> input[name='name'] , #id, .class_name
# driver.find_element(By.CSS_SELECTOR, 'input[name='name']').send_keys("shruti")
#driver.find_element(By.XPATH, "//input[@type='submit]").click()
#driver.find_element(By.CSS_SELECTORS, "inlineRadio1").click()


#another way of chessing msg is using assert
# assert "Success" in error_msg

#-----------to add and clear text-------------
#if same type is used in many to specify one we can use this...
# driver.find_element(By.XPATH,"(//input[@type="text"])[3]").send_keys("helloagain")

#the text if we added to clear that ...
# driver.find_element(By.XPATH,"(//input[@type="text"])[3]").clear()

#Static dropdown
# this we can check on  https://rahulshettyacademy.com/angularpractice/
'''
from selenium.webdriver.support.ui import Select
dropdown = Select(driver.find_element(By.XPATH, "//input[@type='submit']"))
dropdown.select_by_index(1) #based upon index
dropdown.select_visible_text("Female) #select_visible_text() :- will select by visible text
dropdown.select_by_value() #to select by value
'''
#Identifiying Static Dropdown using Select class Selenium
# Rahul Shetty Code
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()

#ID, Xpath, CSS-SELECTORS, Classname, name , linkText
driver.find_element(By.Name, 'email').send_keys('hello@gmail.com')
driver.find_element(By.ID, "example").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1".click())

#Xpath - //tagname[@attribute='value'] -> //input[@type = 'submit']
#CSS - tagname[attribute='value'] -> //input[@type='submit'] , #id, .classname
driver.find_element(By.CSS_SELECTOR, "//input[name='name']").send_keys('Rahul')
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

#Static Dropdown - To use Select() - import -'from selenium.webdriver.support.ui import Select'
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1) #by Index
dropdown.select_by_visible_text('Female') #visible Text
# dropdown.select_by_value() #select by value

driver.find_element(By.XPATH,"//input[@type='submit]").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert "Success" in message