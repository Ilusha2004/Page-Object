import time, pytest
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import PurchaseLocators

class ProductPage(BasePage):

     def should_be_product_page(self):
          self.should_be_show_button()
          self.should_be_added_to_basket()
          self.should_be_noticed_about_element_has_been_added()
          self.should_be_notices_price_in_basket()

     def should_be_tested(self):
          self.test_guest_cant_see_success_message_after_adding_product_to_basket()
          self.test_guest_cant_see_success_message()
          self.test_message_disappeared_after_adding_product_to_basket()

     # метод проверки кноки добавить корзину
     def should_be_show_button(self):
          assert self.is_element_present(*PurchaseLocators.ADD_TO_PURCHASE), "Element isn't exist"

     # метод для добавления в корзину
     def should_be_added_to_basket(self):
          button = self.browser.find_element(*PurchaseLocators.ADD_TO_PURCHASE)
          button.click()
          self.solve_quiz_and_get_code()
          time.sleep(5)

     # Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
     def should_be_noticed_about_element_has_been_added(self):
          print(self.is_element_present(*PurchaseLocators.NAME_STUFF))
          name_stuff = self.browser.find_element(*PurchaseLocators.NAME_STUFF)
          print(f"Element has been added in basket: {name_stuff.text}")
          name_text_approve = self.browser.find_element(*PurchaseLocators.HAS_BEEN_ADDED)
          print(name_text_approve.text)
          assert name_text_approve.text == name_stuff.text, "Names aren't correct"

     # Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
     def should_be_notices_price_in_basket(self):
          print("Checking prices")
          price_in_basket = self.browser.find_element(*PurchaseLocators.BASKET_PRICE)
          price_element = self.browser.find_element(*PurchaseLocators.ELEMENT_PRICE)
          print(f"Price in basket: {price_in_basket.text}\nPrice element: {price_element.text}")
          assert price_in_basket.text == price_element.text, "Prices aren't compable"

     def should_be_added_tool_and_check(self):
          self.browser.find_element(*PurchaseLocators.ADD_TO_PURCHASE).click()
          assert self.is_not_element_present(*PurchaseLocators.HAS_BEEN_ADDED), "Element was shown"

     def should_be_check(self):
          assert self.is_not_element_present(*PurchaseLocators.HAS_BEEN_ADDED), "Element was shown"

     def should_added_tool_and_check_with_is_disappeared(self):
          self.browser.find_element(*PurchaseLocators.ADD_TO_PURCHASE).click()
          time.sleep(2)
          assert self.is_disappeared(*PurchaseLocators.HAS_BEEN_ADDED), "Element was shown"
