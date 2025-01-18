from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        current_url = self.browser.current_url
        assert "basket" in current_url, "The URL should contain the 'basket' substring"

    def should_be_empty_basket_message(self):
        try:
            # Найдите элемент с сообщением
            message_empty_basket = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text.strip()
            # Проверьте, что текст соответствует ожиданиям
            assert "Ваша корзина пуста" in message_empty_basket, \
                f"Expected product name 'Ваша корзина пуста' to be in message '{message_empty_basket}'"
        except NoSuchElementException:
            raise AssertionError("Basket empty message is not displayed on the page")

