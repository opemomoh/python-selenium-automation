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
sleep(4)
driver.get('https://www.target.com/')
sleep(4)
sign_in_dropdown = driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
sign_in_dropdown.click()
sleep(4)
target_sign_in = driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
target_sign_in.click()
sleep(4)

cart_is_empty_verification = driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
assert 'Your cart is empty' in cart_is_empty_verification

