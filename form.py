from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the Chrome driver
driver = webdriver.Chrome()

# Navigate to the form URL
form_url = 'https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php'
driver.get(form_url)
driver.find_element(By.NAME, 'name').send_keys('Name')
driver.find_element(By.NAME, 'email').send_keys('email@gmail.com')
driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/form/div[3]/div/div/div[2]/input').click()
driver.find_element(By.NAME, 'mobile').send_keys('123456789')
driver.find_element(By.NAME, 'dob').send_keys('12/31/2004')
driver.find_element(By.NAME, 'subjects').send_keys('English, Math')
driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/form/div[7]/div/div/div[3]/input').click()

s = driver.find_element(By.XPATH, "//input[@type='file']")
s.send_keys("/*FILE PATH*/")

driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/form/div[9]/div/textarea').send_keys('1301 Third St. Chicago')
driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/form/div[10]/div/div[1]/select/option[3]').click()
driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/form/div[10]/div/div[2]/select/option[3]').click()

time.sleep(4000)
driver.close()
