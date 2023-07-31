from selenium.webdriver.common.by import By

class MinzdrRB():
     DOCUMENT_NAME = (By.CSS_SELECTOR, ".document h4")
     DOWNLOAD_DOCUMENT = (By.CSS_SELECTOR, ".document a:nth-child(2)")