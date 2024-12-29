from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class CartItemsPage(BasePage):
    cart_is_empty = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def verify_cart_is_empty(self):
        cart_is_empty_verification = self.find_element(*self.cart_is_empty).text
        assert 'Your cart is empty' in cart_is_empty_verification
