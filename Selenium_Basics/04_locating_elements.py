import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://muntasir101.github.io/Modern-Bank-Portal/")
time.sleep(3)

customer_registration_button = driver.find_element(By.CSS_SELECTOR,"#homeRegisterCustomerBtnMain")

customer_registration_button.click()

full_name = driver.find_element(By.CSS_SELECTOR, "#customerNameReg")
full_name.send_keys("Mr.Alice")

email = driver.find_element(By.CSS_SELECTOR, "#customerEmailReg")
email.send_keys("alice@gmail.com")

password = driver.find_element(By.CSS_SELECTOR, "#customerPasswordReg")
password.send_keys("123456")

initial_deposit = driver.find_element(By.CSS_SELECTOR, "#initialDepositReg")
initial_deposit.send_keys("1000")

register_button = driver.find_element(By.CSS_SELECTOR, "form[id='customerRegisterForm'] button[type='submit']")
register_button.click()

time.sleep(5)

back_to_home_button = driver.find_element(By.CSS_SELECTOR,"form[id='customerRegisterForm'] button[type='button']")
back_to_home_button.click()

customer_login_button = driver.find_element(By.CSS_SELECTOR, "#homeLoginCustomerBtnMain")
customer_login_button.click()

customer_login_email = driver.find_element(By.CSS_SELECTOR, "#loginEmail")
customer_login_email.send_keys("alice@gmail.com")

customer_login_password = driver.find_element(By.CSS_SELECTOR, "#loginPassword")
customer_login_password.send_keys("123456")

login_button = driver.find_element(By.CSS_SELECTOR, "form[id='loginForm'] button[type='submit']")
login_button.click()

time.sleep(5)
