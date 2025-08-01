import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# setup logging
logging.basicConfig(
    filename="logs/13_log.log",
    level= logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Staring Browser Session...")

driver = webdriver.Firefox()
logging.info("Browser Launch Successfully.")

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
logging.info("URL Open Successfully.")

try:
    wait = WebDriverWait(driver, 20)
    js_alert = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='jsAlert()']")))
    js_alert.click()
    logging.info("Click on JS Normal Alert")

    js_alert_title = driver.switch_to.alert.text
    logging.info(js_alert_title)

    driver.switch_to.alert.accept() # click on ok
    logging.info("Alert Accept.")

except Exception as e:
    logging.info("Element 'JS Alert Button' not found with Explicit wait.")

logging.info("Script Complete.")

driver.quit()

logging.info("End Browser Session...")