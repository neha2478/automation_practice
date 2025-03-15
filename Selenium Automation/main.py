#Here we will copy a code from the doc of Selenium with Python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#to import time module
import time

driver = webdriver.Chrome() #here we will use the Firefox()
driver.get("http://www.python.org") #Going to the python.org
assert "Python" in driver.title #serching wheather python is there in title / not
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source #we are checking "No result found " in deiver.page_source
time.sleep(6) # to sleep it for some time, give sec in function parameter 
driver.close()