from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:/Users/PC/Desktop/python/Selenium_Series/chromedriver.exe")

driver.get("https://login.yahoo.com/")



user_ele = driver.find_element("xpath","//*[@id='login-username']")

user_ele.send_keys("pentest053@gmail.com")
time.sleep(5)

nextbutton = driver.find_element("xpath","//*[@id='login-signin']").click()
time.sleep(5)

pwd = driver.find_element("xpath","//*[@id='password-container']")

pwd.send_keys("weareverydangerous")
time.sleep(10)








