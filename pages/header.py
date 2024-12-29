from locators import driver
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class Header(BasePage):
    target_search_field = driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")
    target_search_button = driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    cart_icon = driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']")

    def search_product(self):
        self.input_text("tea", *self.target_search_field)
        self.click(*self.target_search_button)
        sleep(10)

    def cart_button(self):
        self.click(*self.cart_icon)
        sleep(10)
