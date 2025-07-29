from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()

driver.implicitly_wait(5)

driver.get("https://google.com")

driver.save_screenshot("Google.png")
print("Screenshot Captured.")

driver.quit()