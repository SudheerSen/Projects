from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="C:/Users/PC/Desktop/python/Selenium_Series/chromedriver.exe")

#driver.implicitly_wait(5)
driver.get("https://www.facebook.com/login/")   #opening url takes some time 



print(driver.title)
assert "Log in to Facebook" in driver.title  #assert is verify that is title is true or not 

driver.find_element(By.XPATH,"//*[@id='email']").send_keys("87675575")  #username box
time.sleep(5)

driver.find_element(By.XPATH,"//*[@id='pass']").send_keys("you are bad boy")  #password box
time.sleep(5)

driver.find_element(By.NAME,"login").click()  #login button
time.sleep(5) 