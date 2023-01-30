from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:/Users/PC/Desktop/python/Selenium_Series/chromedriver.exe")

driver.get("http://www.seleniumframework.com/demo-sites/")

links = driver.find_elements(By.TAG_NAME,"a")
print("Number of links present",len(links))  # how many links present in a page

 # how many links are present in the poge
for link in links:
    print(link.text)


 #clicking on link  ----> two methon for clicking link--> 1.link_text,2.partial_link_text
 
#driver.find_element(By.LINK_TEXT,"TUTORIALS").click()
time.sleep(2)

driver.find_element(By.PARTIAL_LINK_TEXT,"FORU").click()

driver.execute_script("windows.ScrollTo(0,100);")


time.sleep(4)