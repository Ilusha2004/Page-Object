import pytest
from selenium.common.exceptions import NoSuchElementException

class Base():
     def __init__(self, browser, url, timeout=10) -> None:
          self.browser = browser
          self.url = url
          self.browser.implicitly_wait(timeout)

     def open_page(self):
          self.browser.get(self.url)

     def is_element_present(self, how, what):
          try:
               self.browser.find_element(how, what)
          except NoSuchElementException:
               return False
          return True
