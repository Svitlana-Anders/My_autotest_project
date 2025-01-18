from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, "button[type='submit'].btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alert:nth-child(1) div.alertinner strong")
    MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, "div.alert:nth-child(3) div.alertinner strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, "//a[contains(@class, 'btn-default') and text()='Посмотреть корзину']")


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.ID, "content_inner")