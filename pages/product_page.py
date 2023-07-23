import time
from .base_page import BasePage
from .locators import PurchaseLocators

class ProductPage(BasePage):

     def should_be_product_page(self):
          self.should_be_show_button()
          self.should_be_added_to_basket()

     # метод проверки кноки добавить корзину
     def should_be_show_button(self):
          assert self.is_element_present(*PurchaseLocators.ADD_TO_PURCHASE), "Element isn't exist"

     # метод для добавления в корзину
     def should_be_added_to_basket(self):
          button = self.browser.find_element(*PurchaseLocators.ADD_TO_PURCHASE)
          button.click()
          self.solve_quiz_and_get_code()
          time.sleep(10)
