from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://muntasir101.github.io/Movie-Ticket-Booking/")

try:
    wait = WebDriverWait(driver, 20)
    ticket_class = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#price")))
    ticket_class_dropdown = Select(ticket_class)

    actual_price_options = []
    print("Ticket Class Dropdown Options: ")
    for dropdown_options in ticket_class_dropdown.options:
        options_text = dropdown_options.text
        print(options_text)
        actual_price_options.append(options_text)

    print(actual_price_options)

    expected_options = ['Regular - $500', 'Silver - $750', 'Gold - $1000', 'Platinum - $1500', 'VIP - $2000']

    if expected_options==actual_price_options:
        print("Ticket Class Dropdown have all options available.")
    else:
        print("Ticket Class Dropdown dont have all options available.")

    ticket_class_dropdown.select_by_value("750")

except Exception as e:
    print("Element 'Ticket Class' not found with Explicit wait.")

try:
    wait = WebDriverWait(driver, 20)
    registered_user = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#user")))
    registered_user_dropdown = Select(registered_user)
    registered_user_dropdown.select_by_value("no")

except Exception as e:
    print("Element 'Register User' not found with Explicit wait.")