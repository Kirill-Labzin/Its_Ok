from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def go_to_add_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket.click()

