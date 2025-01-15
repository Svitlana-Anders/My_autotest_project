from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        add_to_cart_button.click()

    def should_be_message_about_adding(self):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME)
        return message.text.split(":")[1].strip()

    def should_be_message_with_basket_value(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.strip()
        basket_value = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_PRICE).text.split(":")[1].strip()
        assert product_price == basket_value, f"Expected '{ProductPageLocators.PRODUCT_PRICE}' but got '{basket_value}'"


