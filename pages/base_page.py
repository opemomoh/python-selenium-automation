class BasePage:

    def __int__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def click(self, *locators):
        self.driver.find_element(*locators).click()

    def find_element(self, *locators):
        return self.driver.find_element(*locators)

    def find_elements(self, *locators):
        return self.driver.find_elements(*locators)

    def input_text(self, text, *locators):
        self.driver.find_element(*locators).send_keys(text)
