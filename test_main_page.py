import time, pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()
    main_page = LoginPage(browser, browser.current_url)
    main_page.should_be_login_page() # выполняем метод страницы — переходим на страницу логина

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
     # main page
     link = "http://selenium1py.pythonanywhere.com/en-gb/"
     page = MainPage(browser, link)
     page.open()                                # Гость открывает главную страницу
     page.go_to_basket()                        # Переходит в корзину по кнопке в шапке сайта

     new_page = BasketPage(browser=page.browser, url=page.url)
     new_page.should_basket_is_empty()          # Ожидаем, что в корзине нет товаров
     new_page.should_be_send_basket_is_empty()  # Ожидаем, что есть текст о том что корзина пуста