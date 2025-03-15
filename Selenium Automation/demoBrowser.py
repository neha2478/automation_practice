#here we will learn from Intro

#In selenium Package there is a class called webdriver
from selenium import webdriver

#Any of them we can use
# from datetime import time
import time

#with this simple step we can invoke the chrome Driver
#Chrome driver servies is in middle of the webdriver and Chrome() , chrome() will take permission from services
#chrome - will check the current version
#Chrome driver service Selenium 133 -> 133 Chrome driver
driver = webdriver.Chrome() #driver - is obj

#Annother way of using the chromedriver is 
#here manually we are giving path
# service_obj = Service("C:\Users\SHRUTI KARMAKAR\Downloads\chromedriver-win64 (1)\chromedriver-win64")
# webdriver.chrome(service=service_obj)

#to access any website - to get URL
driver.get("https://remoteok.com/")

#time.sleep() - From date and time moduule we can use method sleep() 
#To rest sleep for some times so that we can observe the execution result in website
#Because in selenium after execution the browser will close automaticaly.
time.sleep(2)

