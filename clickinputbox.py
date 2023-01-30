from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="C:/Users/PC/Desktop/python/Selenium_Series/chromedriver.exe")
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")    
time.sleep(2)  

  # How many boxes in form page
inputboxes=driver.find_elements(By.CLASS_NAME,'text_field')  
print("input boxes=",len(inputboxes))  
  
  # check condition that box is displayed or not 
status = driver.find_element(By.ID,"RESULT_TextField-1").is_displayed()
print(status) # true/false

status = driver.find_element(By.ID,"RESULT_TextField-1").is_enabled()
print(status) #enabled or not 
  
time.sleep(2)  
  
  # How to provide the value in text box
driver.find_element(By.ID,"RESULT_TextField-1").send_keys('james')
driver.find_element(By.ID,"RESULT_TextField-2").send_keys('bond')
driver.find_element(By.ID,"RESULT_TextField-3").send_keys('767393939')
driver.find_element(By.ID,"RESULT_TextField-4").send_keys('Dubai')
driver.find_element(By.ID,"RESULT_TextField-5").send_keys('joheh')
driver.find_element(By.ID,"RESULT_TextField-6").send_keys('bondjames@gmail.com')
time.sleep(5)  #taking time to see the result









    