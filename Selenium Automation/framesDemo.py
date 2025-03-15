#So here we will Learn about Frames in Selenium WebDriver
#Frames are emebed on Top of HTML 
#driver will have access to Local Html page only
#It will not access to the embedded frames coz that's an outside art piece.
#Just Like Child windows we need to use some seperate things.

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() 
driver.maximize_window()
print(driver.title) #This will peint Title
print(driver.current_url) #it will print current URL
driver.implicitly_wait(2) #Global wait.

driver.get('https://the-internet.herokuapp.com/iframe') #fetching the webapage

#switch to frames 
driver.switch_to.frame('mce-to-ifr')
#clear() - clear the text
# body - go with that inside p tag is there , so to targrt it use body
driver.find_element(By.ID,'tinymce').clear()

#now after cleaing send keys ...
driver.find_element(By.ID, 'tinymce').send_keys('I am able to automate frames')

#switch to default content - Outside webpage we can use, Come outside of frames
driver.switch_to.default_content()
#here it will fetch the heading in web page and print it , using text 
print(driver.find_element(By.CSS_SELECTOR, "h3").text)
