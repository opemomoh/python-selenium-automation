from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Cart icon')
def click_cart_icon(context):
    context.app.header.cart_button()
    #context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    #sleep(4)


@then('Verify “Your cart is empty” message is shown')
def verify_cart_is_empty(context):
    context.app.cart_item_page.verify_cart_is_empty()
    #cart_is_empty_verification = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    #assert 'Your cart is empty' in cart_is_empty_verification
