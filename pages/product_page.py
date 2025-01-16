from .base_page import BasePage
from .locators import ProductPageLocators
import re
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        add_to_cart_button.click()

    def should_be_message_about_adding(self):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME)
        return message.text.strip()

    def should_be_message_with_basket_value(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.strip()
        basket_value = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_PRICE).text.strip()
        assert re.findall(r'\d+\.?\d*', product_price) == re.findall(r'\d+\.?\d*', basket_value), \
            f"Expected basket value '{product_price}', but got '{basket_value}'"

    def should_be_message_with_goods_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text.strip()
        message_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text.strip()
        assert product_name == message_product_name, \
            f"Expected product name '{product_name}' to be in message '{message_product_name}'"

