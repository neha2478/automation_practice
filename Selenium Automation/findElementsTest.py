#Handling Autosuggestive Dynamic dropdowns using Selenium Webdriver
#Get Attribute value to validateDynamic Text on the Browser
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

#Select the Country name, Autosuggestive dropdown -ind it will show suggestions
driver.find_element(By.ID, "autosuggest").send_keys("ind")

#here if we write ind than 3 suggestions are given than in that drop down if we calick than 3 tags we will found

time.sleep(2) #It will slepp for 2 seconds

#it will select all the elemnts which is matiching to CSS_SELECTORS
#Storing to one variable
#find_elements() - Select Multiple Elements 
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries)) #3

#To iterate through this..countries
# country.text (TEXT is Extracted!!) 
#click() - To click on that
for country in countries:
    if country.text == "India":
        country.click() #hence it is showing that India is selected
        break

#This will print which we selected 
# print(driver.find_element(By.ID, "autosuggest").text) 
#This type of Text we can't returive using Seleniumas we refresh the page the selection will go.
#The things on age which is already there it can be selected not which we made changes

#Using Js there is a value set , we can retive data from there
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"

time.sleep(3)

driver.close()