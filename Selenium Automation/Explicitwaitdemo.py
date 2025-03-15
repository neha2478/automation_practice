#Here we will Learn About Explict and Implict Waits ...
#Specially about Explicit wait....
#Here we will Deep Dive into Functional Automation Using Python :- 
#here we are Assignment - 2

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

expectedList = ['Cucumber - 1 kg', 'Raspberry - 1/4 kg', 'Strawberry - 1/4 kg']
actualList = [] #This we will fetch with code

driver = webdriver.Chrome() # or Edge() or Firefox()...
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

#Using Implict wait
driver.implicitly_wait(2)

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
    #here we will fetch each elements name 
    actualList.append(result.find_element(By.XPATH, "./h4").text)
    #Click on results's each button
    result.find_element(By.XPATH, "div/button").click() #Click on 3 button

# print(f"Expected count: {len(expectedList)}, Actual count: {len(actualList)}")
assert [item.lower() for item in expectedList] == [item.lower() for item in actualList] #This assert working 


#This one Check Cart Operation 
#CSS Selector - img[alt='Cart']
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click() #click onCart
# //button[text()='PROCEED TO CHECKOUT'] - button - text() - to fetch the text value if same

#Click on Proceed-to-checkout-button
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# time.sleep(4)

#Checking Functional Automation using Python
# Here we will Try to add the Total in Kart page and check weather it is equal to the Total Amount 
#SUM Validation

prices = driver.find_elements(By.CSS_SELECTOR, 'tr td:nth-child(5) p')
sum = 0
# iterate though each elemnent
for price in prices:
    sum = sum + int(price.text)       #48 + 160+ 180 , int() to convert in integer

print(sum)

#here string will be exteacted so int() - Convert in integer
total_amount = int(driver.find_element(By.CSS_SELECTOR, '.totAmt').text) 

assert sum == total_amount


#using CSS_Selectors , .promocode
#here we will put promocode 
driver.find_element(By.CSS_SELECTOR, ".promocode").send_keys('rahulshettyacademy')

#Click on Apply button
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()

#here to fetch the promocode itmay take more than 5 sec so we will use Explicit waits ,
#It will override the code.
wait = WebDriverWait(driver, 10) #wait - Obj , here WebDriverWait(diver, time)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.promoInfo'))) #here the promoinfo is taking time more so here the condition is on that 
#expected_conditioms - to put condition on that
#presence_of_located - will check weather it is located or not till then it will wait.

# time.sleep(5)

#Promo code applied
print(driver.find_element(By.CSS_SELECTOR, '.promoInfo').text)

#Click on PlaceOrder button
# driver.find_element(By)

time.sleep(3)

#here Dicount amount < Total Amount 
discount_amount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

assert discount_amount < total_amount


#O/P :- 
'''
DevTools listening on ws://127.0.0.1:51584/devtools/browser/a16cf50d-60ed-419e-b81e-4151b333e1b7
The count of ele : 3
Code applied ..!
Created TensorFlow Lite XNNPACK delegate for CPU.
Attempting to use a delegate that only supports static-sized tensors with a graph that has dynamic-sized tensors (tensor#-1 is a dynamic-sized tensor).
'''
#Updated code O/P - SUM VALIDATOR incluced
'''
DevTools listening on ws://127.0.0.1:51584/devtools/browser/a16cf50d-60ed-419e-b81e-4151b333e1b7
The count of ele : 3
388
Code applied ..!
Created TensorFlow Lite XNNPACK delegate for CPU.
Attempting to use a delegate that only supports static-sized tensors with a graph that has dynamic-sized tensors (tensor#-1 is a dynamic-sized tensor).
'''