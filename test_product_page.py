from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .locators import ProductPageLocators
import time



def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_product_to_basket()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    time.sleep(4)
    page.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
    page.should_be_message_about_adding()
    page.should_be_message_with_basket_value()
