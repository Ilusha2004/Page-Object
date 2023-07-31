import time
from .base import Base
from .locators import MinzdrRB

class MainPage(Base):

     def should_start(self):
          self.should_check_elements()
          self.should_find_elements()
          self.regex_tags()
          self.should_be_select_needles()

     def __init__(self, browser, url, timeout=10) -> None:
          super().__init__(browser, url, timeout)
          self.__tags : list = []
          self.__names : list = []
          self.__selected_titles : list = []

     def should_check_elements(self):
          print("Checking elements...")
          assert self.is_element_present(*MinzdrRB.DOWNLOAD_DOCUMENT) == self.is_element_present(*MinzdrRB.DOCUMENT_NAME), "NSE"

     def should_find_elements(self):
          print("Finding elements...")
          names = self.browser.find_elements(*MinzdrRB.DOCUMENT_NAME)
          tags_temp = self.browser.find_elements(*MinzdrRB.DOWNLOAD_DOCUMENT)

          # title of text
          for name in names:
               temp = name.text.split("(")
               self.__names.append(temp[0] + temp[1])

          print("Showing titles:")

          for name in self.__names:
               print(name)

          # href tags
          for tag in tags_temp:
               self.__tags.append(tag)

          print("Showing tags:")

          for tag in self.__tags:
               print(tag.get_attribute('href'))

     def regex_tags(self):
          with open("parser/test.txt", 'r') as file_1, open("parser/text.txt") as file_2:
               names_1 = []
               names_2 = []

               for line in file_1:
                    temp = line.split("(")
                    try:
                         names_1.append(temp[0] + temp[1])
                    except:
                         pass

               for line in file_2:
                    temp = line.split("(")
                    try:
                         names_2.append(temp[0] + temp[1])
                    except:
                         pass

               for line_1 in names_1:
                    for line_2 in names_2:
                         if line_1.lower() == line_2.lower():
                              self.__selected_titles.append(line_1)

     def should_be_select_needles(self):
          for item in zip(self.__names, self.__tags):
               if self.__selected_titles.count(item[0]) > 0:
                    print(f"Downloading: {item[0]}...")
                    item[1].click()
                    item[1].click()
                    time.sleep(5)
