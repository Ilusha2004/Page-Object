import time
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # проверкa на корректный url адрес
    def should_be_login_url(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_URL).click()
        print(self.browser.current_url)
        assert self.browser.current_url, "link is not responed"

    # проверкa, что есть форма логина
    def should_be_login_form(self):
        print(*LoginPageLocators.LOGIN_FORM_USERNAME)
        print(LoginPageLocators.LOGIN_FORM_USERNAME[1])
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_USERNAME), "missing element: Email"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_PASSWORD), "missing element: Password"

    # проверкa, что есть форма регистрации на странице
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM_USERNAME), "missing element: Email"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM_PASSWORD), "missing element: Password"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM_REPEAT_PASSWORD), "missing element: Repeat Password"

    def register_new_user(self, email, password):
        email_send = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_USERNAME)
        email_send.send_keys(email)
        pass_send = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASSWORD)
        pass_send.send_keys(password)
        repeat_send = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_REPEAT_PASSWORD)
        repeat_send.send_keys(password)

    def should_be_user_registered(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_VALID), "Registration was occuring"
