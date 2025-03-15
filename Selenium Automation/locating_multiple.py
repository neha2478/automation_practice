#Here Locating Multiple Elements in web pages :-
#to go to next page we will inglude page link to URL driver.get()...
#to print elemnts 
#to print elemets in for Loop

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

# driver = webdriver.Chrome()
# query = "laptop"
# for i in range(1, 20):
#     driver.get(f'https://www.amazon.in/s?k={query}&page{i}2&crid=3NAVORZL79D7R&sprefix=laptop%2Caps%2C317&ref=nb_sb_noss_2')

#     #to sech multple element - driver.fing_elements()
#     elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")

#     # print(elems)

#     print(f"{len(elems)} items found")

#     #if we want to print elements using for Loop
#     for e in elems:
#         print(e.text)

#     time.sleep(2)

#     driver.close()

driver = webdriver.Chrome() 
query = "Laptop"
driver.get(f'https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')

# Wait for the page to load (use a short sleep or explicit wait for better reliability)
time.sleep(3)

# Locate elements by the specified class name
elems = driver.find_elements(By.CLASS_NAME, "tUxRFH")
# print(elems)

# Print the text of each element found
if elems:
    print(f"Number of elements found: {len(elems)}")
    for elem in elems:
        print(elem.text)
else:
    print("No elements found!") 

# print(f'Number of elements found : {len(elems)}')
# for elem in elems:
#     print(elem.text)

# Close the browser after a short delay
time.sleep(2)
driver.close()
