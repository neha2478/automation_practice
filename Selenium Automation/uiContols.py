#Handling Checkbox using Selenium Python Programming
#Understand radiobutton Automation with Example

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome() #we can use Firefox() or Edge()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# 1> Task - Handling Checkbox
'''
We can know option-2 position it may change later so we are taking this process
Here we will not use Id, name, class we will use other attributes .
find_elements() - Will be use to fetch Multiple elemnts 
get_attribute() - fetch Dynamic Values, as it is similar to our check box or not
the get_attribute('value'), type or other things
is_selected() - Selenium Method - To check box is selected or not 
'''
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes), checkboxes)

for checkbox in checkboxes:
    if checkbox.get_attribute('value') == 'option2':
        checkbox.click() #To select the checkbox
        checkbox.is_selected() #Selenium method - check weather selected or not
        break

# Task-2 :- Radio Button
'''
Here we will use the CSS_SELECTORS , take class ...
findelements() :- To select multiple no of elements of same condition
Radio buttons won't change so no need to iterate
is_selected() - check weather selected or not for particular ele
'''
radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[2].click() #click() will select the 2 radio button , 2 - index val
assert radiobuttons[2].is_selected()



#Task -3 :- Test on Element Displayed or not
'''
is_displayed() - will check displayed or not
'''
# '#displayed-text' - for text box ...
assert driver.find_element(By.ID, "displayed-text").is_displayed() #here it will be displayed
driver.find_element(By.ID, "hide-textbox").click() #Click on Hide button
assert not driver.find_element(By.ID, "displayed-text").is_displayed() #Check test box is displayed or not

time.sleep(5)
driver.close()

#O/P 1:-
'''
DevTools listening on ws://127.0.0.1:64925/devtools/browser/dbffe7a2-861b-4176-a4da-ef2bb645e3af
3 [<selenium.webdriver.remote.webelement.WebElement (session="c487f59022bb8dc871eb237525c29c0d", element="f.0F82883337B3D5F31101A4350880C5D5.d.4B4F62E6DDE36C3858CE23FB25D65FCF.e.7")>, <selenium.webdriver.remote.webelement.WebElement (session="c487f59022bb8dc871eb237525c29c0d", element="f.0F82883337B3D5F31101A4350880C5D5.d.4B4F62E6DDE36C3858CE23FB25D65FCF.e.8")>, <selenium.webdriver.remote.webelement.WebElement (session="c487f59022bb8dc871eb237525c29c0d", element="f.0F82883337B3D5F31101A4350880C5D5.d.4B4F62E6DDE36C3858CE23FB25D65FCF.e.9")>]
'''
#O/P 2:- After changes in code
'''
DevTools listening on ws://127.0.0.1:49353/devtools/browser/80b01c8b-013a-48a0-89a8-e4f5a8b24e13
3 [<selenium.webdriver.remote.webelement.WebElement (session="2f0b5bd0c4c6b33b531f8ea11e6ffd2b", element="f.362C4DF210B725C8FE3D0F25B3CB0D15.d.7FBC7C5E88A5A2023A822B918BBB28F7.e.10")>, <selenium.webdriver.remote.webelement.WebElement (session="2f0b5bd0c4c6b33b531f8ea11e6ffd2b", element="f.362C4DF210B725C8FE3D0F25B3CB0D15.d.7FBC7C5E88A5A2023A822B918BBB28F7.e.11")>, <selenium.webdriver.remote.webelement.WebElement (session="2f0b5bd0c4c6b33b531f8ea11e6ffd2b", element="f.362C4DF210B725C8FE3D0F25B3CB0D15.d.7FBC7C5E88A5A2023A822B918BBB28F7.e.12")>]
'''
#O/P 3 :- 
'''
3 [<selenium.webdriver.remote.webelement.WebElement (session="99538548d8064e17afc4b9d90fe0d6e5", element="f.8BE0B606511B8FC1AE798DAFC8341160.d.6306DC30FCCEB02A90D94FFBB08ABA12.e.9")>, <selenium.webdriver.remote.webelement.WebElement (session="99538548d8064e17afc4b9d90fe0d6e5", element="f.8BE0B606511B8FC1AE798DAFC8341160.d.6306DC30FCCEB02A90D94FFBB08ABA12.e.10")>, <selenium.webdriver.remote.webelement.WebElement (session="99538548d8064e17afc4b9d90fe0d6e5", element="f.8BE0B606511B8FC1AE798DAFC8341160.d.6306DC30FCCEB02A90D94FFBB08ABA12.e.11")>]
'''