from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:/Users/PC/Desktop/python/Selenium_Series/chromedriver.exe")

driver.get("https://login.yahoo.com/")
print(driver.title)


driver.get("https://www.linkedin.com/login")
time.sleep(5)
print(driver.title)


driver.back()      # use this command for back in webdriver
time.sleep(5)
print(driver.title)



driver.forward()     #use this command for forward in webdriver
time.sleep(5)
print(driver.title)




