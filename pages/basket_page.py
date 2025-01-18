from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):
    MESSAGES = {
        "en": "Your basket is empty",
        "ru": "Ваша корзина пуста",
        "fr": "Votre panier est vide",
        "es": "Tu carrito está vacío"}

    def should_be_basket_page(self):
        assert "basket" in self.browser.current_url, "The URL should contain the 'basket' substring"

    def should_not_have_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"

    def should_be_empty_basket_message(self, language="en"):
        try:
            # Найдите элемент с сообщением
            message_empty_basket = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text.strip()
            expected_message = self.MESSAGES.get(language, "Your basket is empty")
            assert expected_message in message_empty_basket, \
                f"Expected basket message '{expected_message}' to be in message '{message_empty_basket}'"
        except NoSuchElementException:
            raise AssertionError("Basket empty message is not displayed on the page")

