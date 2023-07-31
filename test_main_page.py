from .pages.main_page import MainPage
from selenium.webdriver.common.by import By
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    main_page = LoginPage(browser, browser.current_url)
    main_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
     # main page
     link = "http://selenium1py.pythonanywhere.com/en-gb/"
     # Гость открывает главную страницу
     # Переходит в корзину по кнопке в шапке сайта
     # Ожидаем, что в корзине нет товаров
     # Ожидаем, что есть текст о том что корзина пуста
     page = ProductPage(browser, link)
     page.open()
     pass
