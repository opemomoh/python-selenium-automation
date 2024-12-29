from pages.base_page import BasePage
from pages.header import Header
from pages.main_page import MainPage
from pages.cart_item_page import CartItemsPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page = BasePage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.cart_item_page = CartItemsPage(driver)
