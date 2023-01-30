## Agenda=
# scroll down the page by pixel 
# scroll down the page by element found
# scroll  to end of the page

from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome(executable_path="C:/Users/PC/Desktop/python/Selenium_Series/chromedriver.exe")
driver.get("https://www.google.com/search?client=firefox-b-d&q=james+bond")
driver.maximize_window()
time.sleep(4)


# 1. scroll down page by pixel 
#driver.execute_script("windows.scrollBy(0,1000)","")
#time.sleep(4)

# 2.scroll down the page by element found
flag = driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div[5]/div/div/div/div/div/div/div/div[1]/div/a/div/cite")
driver.execute_script("arguments[0].scrollIntoView();",flag)


time.sleep(5)

