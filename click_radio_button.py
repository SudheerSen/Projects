from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="C:/Users/PC/Desktop/python/Selenium_Series/chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")


# working with radio button

status = driver.find_element(By.ID,'RESULT_RadioButton-7_0').is_selected() ## radio button present or not ,true/false
print(status)

driver.find_element(By.ID,'RESULT_RadioButton-7_0').click()

status = driver.find_element(By.ID,'RESULT_RadioButton-7_0').is_selected()
print(status)


 # scroll the page
driver.execute_script("window.scrollTo(0,300);")

time.sleep(3)


# working with check boxes

driver.find_element(By.ID,"RESULT_CheckBox-8_0").click()
time.sleep(2)
driver.find_element(By.ID,"RESULT_CheckBox-8_6").click()
time.sleep(3)


