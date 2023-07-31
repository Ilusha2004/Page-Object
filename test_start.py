import pytest
from .parser.main_page import MainPage

def test_minzdrav(browser):
     link = "https://minzdrav.gov.by/ru/dlya-spetsialistov/standarty-obsledovaniya-i-lecheniya/stomatologiya.php"
     page = MainPage(browser, link)
     page.open_page()
     page.should_start()
