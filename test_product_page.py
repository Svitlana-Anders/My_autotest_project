from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
import pytest

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "Password"
        page.register_new_user(email, password)
        page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.add_product_to_basket()
        page.should_be_message_about_adding()
        page.should_be_message_with_product_price()
        page.should_be_message_with_product_name()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.add_product_to_basket()
    # page.solve_quiz_and_get_code()
    # time.sleep(3)
    page.should_be_message_about_adding()
    page.should_be_message_with_product_price()
    page.should_be_message_with_product_name()


@pytest.mark.parametrize('should_fail', [pytest.param(True, marks=pytest.mark.xfail(reason="Known bug, message does not disappear"))])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, should_fail):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    # page.solve_quiz_and_get_code()
    # time.sleep(3)
    page.should_not_be_success_message()


@pytest.mark.parametrize('should_fail', [pytest.param(True, marks=pytest.mark.xfail(reason="Known bug, message does not disappear"))])
def test_message_disappeared_after_adding_product_to_basket(browser, should_fail):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.message_disappeared_after_adding_product_to_basket()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_not_have_products()
    basket_page.should_be_empty_basket_message()

