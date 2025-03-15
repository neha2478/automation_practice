#here we will Learn how to sort Tables 
#working on GreenKart

from selenium import webdriver
from selenium.webdriver.common.by import By

browserSortedVeggies = [] #Empty List

driver = webdriver.Chrome()

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')
driver.maximize_window() #will maximize windows

driver.implicitly_wait(5)

#click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click() #It will fetch text between tag

#collect all veggie names - BrowserSortedveggieList (B, A, C)
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")

#iterating through elements of veggieWebElements
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

#before sorting we will store in new Variable, So that after shorting it should not be vanish
orignalBrowserSortedList = browserSortedVeggies.copy() #copy of List -so we are using copy()

#sort this veggieList => newSortedList (A, B, C)
browserSortedVeggies.sort() #this will not create new List aftersorting

#BrowserSortedveggieList == newSortedList
assert browserSortedVeggies == orignalBrowserSortedList

print('Task completed!!')

#O/P :-
'''
DevTools listening on ws://127.0.0.1:55527/devtools/browser/2a8fe29f-09f1-4eb6-8761-d27c1ed11f81
Task completed!!
'''
