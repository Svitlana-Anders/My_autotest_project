from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, "The URL should contain the 'login' substring"

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert True

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        assert True

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        input_email.send_keys(email)
        input_password1 = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        input_password1.send_keys(password)
        input_password2 = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT)
        input_password2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()
