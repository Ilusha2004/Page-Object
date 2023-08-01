import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", \
#                                                marks=pytest.mark.xfail(reason="AssertionError: Names aren't correct")),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#      print(link)
#      prod_page = ProductPage(browser, link)
#      prod_page.open()
#      prod_page.should_be_product_page()

# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#      link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
#      # Открываем страницу товара
#      # Добавляем товар в корзину
#      # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
#      prod_page = ProductPage(browser, link)
#      prod_page.open()
#      prod_page.should_be_added_tool_and_check()

# def test_guest_cant_see_success_message(browser):
#      link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
#      # Открываем страницу товара
#      # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
#      prod_page = ProductPage(browser, link)
#      prod_page.open()
#      prod_page.should_be_check()

# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#      link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
#      # Открываем страницу товара
#      # Добавляем товар в корзину
#      # Проверяем, что нет сообщения об успехе с помощью is_disappeared
#      prod_page = ProductPage(browser, link)
#      prod_page.open()
#      prod_page.should_added_tool_and_check_with_is_disappeared()

# def test_guest_should_see_login_link_on_product_page(browser):
#      link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#      page = ProductPage(browser, link)
#      page.open()
#      page.should_be_login_link()

# def test_guest_can_go_to_login_page_from_product_page(browser):
#      # product page
#      link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"
#      page = ProductPage(browser, link)
#      page.open()
#      page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
     # Product list
     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"
     # Гость открывает страницу товара
     # Переходит в корзину по кнопке в шапке
     # Ожидаем, что в корзине нет товаров
     # Ожидаем, что есть текст о том что корзина пуста
     page = ProductPage(browser, link)
     page.open()
     page.go_to_basket()

     new_page = BasketPage(browser=page.browser, url=page.url)
     new_page.should_basket_is_empty()
     new_page.should_be_send_basket_is_empty()