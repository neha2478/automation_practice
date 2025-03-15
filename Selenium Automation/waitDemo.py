#Here we will Learn About Explict and Implict Waits ...

#Espically about Implicit waits ...

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome() # or Edge() or Firefox()...
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

#Using Implict wait
driver.implicitly_wait(5)

# 5 seconds is max time out... 2 seconds - element is displayed, 3 sec to save
#for lines we don't need to have time out , We are using Global Time out..

#to put input in the search bar
driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys('ber')

time.sleep(2)

#Add the Products in cart after search 
#XPATH - "//div[@class= 'products']/div"
results = driver.find_elements(By.XPATH, "//div[@class='products']/div") #List of Elements ... 15 min
count = len(results)
print(f'The count of ele : {count}')
#validationg result using a keyword of Pytest - assert
assert count > 0

#Task - Develop End to End TC to Automate Greenkart
'''
#to find Button in one card 
Xpath :- //div[@class='products']/div/div/button
'''
#Add to Cart 
for result in results:
    #Click on results's each button
    result.find_element(By.XPATH, "div/button").click() #Click on 3 button

#This one Check Cart Operation 
#CSS Selector - img[alt='Cart']
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click() #click onCart
# //button[text()='PROCEED TO CHECKOUT'] - button - text() - to fetch the text value if same

#Click on Proceed-to-checkout-button
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# time.sleep(4)

#using CSS_Selectors , .promocode
#here we will put promocode 
driver.find_element(By.CSS_SELECTOR, ".promocode").send_keys('rahulshettyacademy')

#Click on Apply button
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()

# time.sleep(5)

#Promo code applied
print(driver.find_element(By.CSS_SELECTOR, '.promoInfo').text)

#Click on PlaceOrder button
# driver.find_element(By)

time.sleep(3)


#O/P :-
''' 
DevTools listening on ws://127.0.0.1:52112/devtools/browser/014e6d53-fcb8-49d4-b50a-e9d280b110de
The count of ele : 3'
'''
'''
DevTools listening on ws://127.0.0.1:53117/devtools/browser/0852cad7-6f02-4c67-b771-11c49bb7c131
The count of ele : 3
Created TensorFlow Lite XNNPACK delegate for CPU.
Attempting to use a delegate that only supports static-sized tensors with a graph that has dynamic-sized tensors (tensor#-1 is a dynamic-sized tensor).
Code applied ..!
'''
'''
DevTools listening on ws://127.0.0.1:57749/devtools/browser/246ffa18-6bbd-4b3e-92b9-d4d4ca60e26f
The count of ele : 3
Code applied ..!
'''