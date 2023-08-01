import time
from .languages import languages
from .base_page import BasePage
from .locators import *
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasketPage(BasePage):

     def should_basket_is_empty(self):
          assert self.is_not_element_present(*PurchaseLocators.BASKET_ITEMS), "Your basket isn't empty"

     def should_be_send_basket_is_empty(self):
          self.is_element_present(*PurchaseLocators.BASKET_CONTENT)
          content = self.browser.find_element(*PurchaseLocators.BASKET_CONTENT).text
          message = content.split('.')[0].strip()
          print(message)
          assert message == languages["en-gb"], "Basket is not empty"
