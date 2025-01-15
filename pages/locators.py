from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, "button[type='submit'].btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "col-sm-6 product_main")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "price_color")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "")
    MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, "")

