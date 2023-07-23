from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
     def login_test(self):
          self.go_to_login_page()
          self.should_be_login_link()

     def go_to_login_page(self):
          login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
          login_link.click()
          alert = self.browser.switch_to.alert
          alert.accept()
          # return MainPage(browser=self.browser, url=self.url)

     def should_be_login_link(self):
          assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"