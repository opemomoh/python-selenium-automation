from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

amazon_logo = driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
email_field = driver.find_element(By.ID, 'ap_email')
continue_button = driver.find_element(By.ID, "continue")
conditions_of_use_link = driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
privacy_notice_link = driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
need_help_link = driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
forgot_your_password_link = driver.find_element(By.ID, "auth-fpp-link-bottom")
other_issues_with_signin_link = driver.find_element(By.ID, "ap-other-signin-issues-link")
create_your_amazon_account_button = driver.find_element(By.ID, "createAccountSubmit")
amazon_orders_returns = driver.find_element(By.ID, "nav-cart")
#amazon_signup_page
amazon_logo_signup_page = driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')
create_account_logo = driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
signup_your_name = driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
signup_mobile_number_or_email = driver.find_element(By.CSS_SELECTOR, '#ap_email')
signup_password = driver.find_element(By.CSS_SELECTOR, '#ap_password')
signup_reenter_password = driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
signup_continue = driver.find_element(By.CSS_SELECTOR, '#continue')
amazon_sign_in = driver.find_element(By.CSS_SELECTOR, 'a.a-link-emphasis')

#target_locators
cart_icon = driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']")
sign_in_dropdown = driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
target_sign_in = driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
sign_in_verification = driver.find_element(By.CSS_SELECTOR, '#login')
cart_is_empty_verification = driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
target_circle_link = driver.find_element(By.CSS_SELECTOR, "[href='/circle']")
target_benefit_verification_link = driver.find_element(By.CSS_SELECTOR, "[class*='styles__BenefitsGrid'] li")
target_search_field = driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")
target_search_button = driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
target_addtocart_button = driver.find_element(By.CSS_SELECTOR, "[data-test='addToCartButton']")
target_addtocart_verification = driver.find_element(By.CSS_SELECTOR, "[data-test='addToCartButton']")