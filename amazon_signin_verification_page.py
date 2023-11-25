from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# populate search field
amazon_orders_returns = driver.find_element(By.ID, "nav-orders")
amazon_orders_returns.click()
sleep(4)

sign_in_header_verification = driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small').text
email_input_verification = driver.find_element(By.CSS_SELECTOR, 'label.a-form-label').text

assert 'Sign in' in sign_in_header_verification
assert 'Email or mobile phone number' in email_input_verification
sleep(1)
print("Test Case Passed")