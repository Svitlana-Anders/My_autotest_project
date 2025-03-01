from .base_page import BasePage
from .locators import ProductPageLocators
import re


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        add_to_cart_button.click()

    def should_be_message_about_adding(self):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME)
        assert message, "Message about adding product to basket is not displayed"

    def should_be_message_with_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.strip()
        basket_value = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_PRICE).text.strip()
        assert re.findall(r'\d+\.?\d*', product_price) == re.findall(r'\d+\.?\d*', basket_value), \
            f"Expected basket value '{product_price}', but got '{basket_value}'"

    def should_be_message_with_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text.strip()
        message_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text.strip()
        assert product_name == message_product_name, \
            f"Expected product name '{product_name}' to be in message '{message_product_name}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_NAME), \
           "Success message is presented, but should not be"

    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_PRODUCT_NAME), \
            "Success message is presented, but should not be"

