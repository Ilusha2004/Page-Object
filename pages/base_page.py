import math, time
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import *

class BasePage():
     def __init__(self, browser, url):
          self.browser = browser
          self.url = url

     def go_to_basket(self):
          self.browser.find_element(*PurchaseLocators.VIEW_BASKET).click()

     def go_to_login_page(self):
          self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

     def should_be_authorized_user(self):
          assert self.is_element_present(*BasePageLocators.USER_ICON),\
               "User icon is not presented, probably unauthorised user"

     def should_be_login_link(self):
          assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

     def solve_quiz_and_get_code(self):
          alert = self.browser.switch_to.alert
          x = alert.text.split(" ")[2]
          answer = str(math.log(abs((12 * math.sin(float(x))))))
          alert.send_keys(answer)
          alert.accept()

          if str(self.browser.current_url).count("promo=newYear2019") > 0:    # If we get more than 0 we gonna click alert twice
               WebDriverWait(self.browser, 30).until(EC.alert_is_present())

          try:
               alert = self.browser.switch_to.alert
               alert_text = alert.text
               print(f"Your code: {alert_text}")
               alert.accept()
          except NoAlertPresentException:
               print("No second alert presented")

     # True if element exist
     def is_element_present(self, how, what, timeout=10):
          try:
               WebDriverWait(self.browser, timeout, 1, NoSuchElementException).\
                    until(EC.presence_of_element_located((how, what)))
          except NoSuchElementException:
               return False

          return True

     # False if element will show
     def is_disappeared(self, how, what, timeout=4):
          try:
               WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                    until_not(EC.presence_of_element_located((how, what)))
          except TimeoutException:
               return False

          return True

     # True if element won't show
     def is_not_element_present(self, how, what, timeout=4):
          try:
               WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
          except TimeoutException:
               return True

          return False

     def open(self):
          self.browser.get(self.url)