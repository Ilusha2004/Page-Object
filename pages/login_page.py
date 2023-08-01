import time
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверкa на корректный url адрес
        self.browser.find_element(*LoginPageLocators.LOGIN_URL).click()
        time.sleep(3)
        print(self.browser.current_url)
        assert self.browser.current_url, "link is not responed"

    def should_be_login_form(self):
        # проверкa, что есть форма логина
        print(*LoginPageLocators.LOGIN_FORM_USERNAME)
        print(LoginPageLocators.LOGIN_FORM_USERNAME[1])
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_USERNAME), "missing element: Email"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_PASSWORD), "missing element: Password"

    def should_be_register_form(self):
        # проверкa, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM_USERNAME), "missing element: Email"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM_PASSWORD), "missing element: Password"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM_REPEAT_PASSWORD), "missing element: Repeat Password"