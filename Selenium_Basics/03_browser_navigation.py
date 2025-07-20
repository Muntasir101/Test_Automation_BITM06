import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://google.com")
time.sleep(3)

driver.get("https://apple.com")
time.sleep(3)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()

driver.quit()

