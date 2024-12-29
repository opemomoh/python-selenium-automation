from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Search for your {product}')
def input_product_in_the_search_field(context, product):
    search_field = context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")
    search_field.clear()
    search_field.send_keys("table")
    sleep(4)


@when('Click on target search icon')
def click_on_search(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(4)


@when('Click product image')
def click_prodict_image(context):
    context.driver.find_element(By.CSS_SELECTOR, "picture[data-test*='ProductCard/ProductCardImage']").click()
    sleep(5)


@when('Add to cart')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']").click()
    sleep(5)


@then('Verify {product} is added to cart')
def verify_product_added_to_cart(context, product):
    addedtocart_verification = context.driver.find_element(By.CSS_SELECTOR, ".h-text-lg").text
    assert "Added to cart" in addedtocart_verification, f'Expected Added to cart but got {addedtocart_verification}'
#test for my git push