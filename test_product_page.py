from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import time
import pytest


# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

@pytest.mark.parametrize('promo_offer', [1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_product_to_basket()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    time.sleep(3)

    page.should_be_message_with_basket_value()
    page.should_be_message_with_goods_name()


