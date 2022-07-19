from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        time.sleep(5)
        assert "login" in self.browser.current_url, "Login link is not correct" # current_url чекает текущий url
        # реализуйте проверку на корректный url адрес


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Not have login form"
        # реализуйте проверку, что есть форма логина


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Not have register form"