from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time 

driver = webdriver.Chrome() #from webdriver we are passing a Chrome() 
query = 'Laptop' #here we are passing a query 
driver.get(f'https://www.amazon.in/s?k={query}&crid=3NAVORZL79D7R&sprefix=laptop%2Caps%2C317&ref=nb_sb_noss_2')
#int get () we are passing a URL 

#find Element - is the method to find Element.
ele = driver.find_element(By.CLASS_NAME, "puis-card-container")
# print(ele.text) #here we will print the text
print(ele.get_attribute("outerHTML")) #write Htnl in Caps

time.sleep(2)
driver.close()