# Advanced Interactions with bowser elements using Action class :- 

#LEARN TO USE ACTION CLASS :-
'''
1> Learn how to hover on that withou performing anuy actions..
2> Than perform  Click on Top 
3> Click on Mouse Hover 
4> perform() - Than only sequence of obj will perform
5> ActionChains() #pass driver as arg

6> click_and_hold(), content_click(), drag_and_drop(), double_click(), move_to_element()
'''

# Automation on website :- https://rahulshettyacademy.com/AutomationPractice/

#code 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains #importing ActionChains

driver = webdriver.Chrome() #here using firefix() //Chrome() or Edge()
driver.maximize_window()

driver.implicitly_wait(5)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

action = ActionChains(driver)
#here it will just hover on this
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform() #is on of the function of action
#will click on Top
# action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
#click on Relode in Dropdown
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()

print('Hi your task Finished!!')

# O/P:-
'''
DevTools listening on ws://127.0.0.1:58621/devtools/browser/e7cb0a64-989e-44e4-a737-ef1b62fa9e0e
Hi your task Finished!!
'''