#here we will Learn about the how to access the Child
'''
The selenium can aceess the Link 
The child window is directly not accessable 
Their are other ways to do 
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
# print(driver.title) #Extra

driver.get("https://the-internet.herokuapp.com/windows")

#Using Implicit wait
driver.implicitly_wait(2)

#click on the Click here Link , Using Link Text
driver.find_element(By.LINK_TEXT,'Click Here').click()

windowsOpenedList = driver.window_handles # window_handles fetch all the windows in form of List
# In List [] , 0 index - parent List , 1 index - Child List

driver.switch_to.window(windowsOpenedList[1]) #to switch in Child windows.

driver.find_element(By.TAG_NAME, "h3").text #fetching the child window Text

driver.close() #close the driver

driver.switch_to.window(windowsOpenedList[0]) #Switching back to parent window

assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text

print('Assertion Passed!!, Task Completed Successfully!!')


#O/P :- 
'''
DevTools listening on ws://127.0.0.1:61864/devtools/browser/5190f572-b9e0-4440-8c1c-9f2b587396a5

Assertion Passed!!, Task Completed Successfully!!
'''
