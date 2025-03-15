import time
from selenium import webdriver

#driver - obj create by use , stores the webdriver.Chrom() in it
driver = webdriver.Edge()
driver.get("https://remoteok.com/") #fetch URL

#To maximize window we use - maximize_window()
driver.maximize_window()

#title() - To fetch the Tiltle of the web page
print(driver.title) #print() will print the title.

#current_url :-To fetch the current URl of the Plage
print(driver.current_url)

time.sleep(3) #sleep() - will sleep for secs
driver.close() # close() - it will close the driver

# O/P :- 
'''
DevTools listening on ws://127.0.0.1:55646/devtools/browser/4e4ad966-76fd-4efa-9428-e887048d546a
Remote Jobs in Programming, Design, Sales and more #OpenSalaries
https://remoteok.com/
'''

#if we want to run on Different browsers than we can use Firefox() , Edge()
#similarly we can install the edge and chrome drivers , for edge is edge , for Firefox - Gecko driver
#this same as manually we did for chrome driver.., path of Driver 