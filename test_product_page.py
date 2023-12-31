import pytest, time
import configparser
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",\
                                               marks=pytest.mark.xfail(reason="AssertionError: Names aren't correct")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
     prod_page = ProductPage(browser, link)
     prod_page.open()
     prod_page.should_be_product_page()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
     prod_page = ProductPage(browser, link)
     prod_page.open()    # Открываем страницу товара
                                                # Добавляем товар в корзину
     prod_page.should_be_added_tool_and_check() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

def test_guest_cant_see_success_message(browser):
     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
     prod_page = ProductPage(browser, link)
     prod_page.open()              # Открываем страницу товара
     prod_page.should_be_check()   # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
     prod_page = ProductPage(browser, link)
     prod_page.open()              # Открываем страницу товара
                                                                 # Добавляем товар в корзину
     prod_page.should_added_tool_and_check_with_is_disappeared() # Проверяем, что нет сообщения об успехе с помощью is_disappeared

def test_guest_should_see_login_link_on_product_page(browser):
     link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
     page = ProductPage(browser, link)
     page.open()
     page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
     link = "http://selenium1py.pythonanywhere.com/catalogue/"  # Product list
     page = ProductPage(browser, link)
     page.open()
     page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
     link = "http://selenium1py.pythonanywhere.com/catalogue/"  # Product list
     page = ProductPage(browser, link)
     page.open()                                   # Гость открывает страницу товара
     page.go_to_basket()                           # Переходит в корзину по кнопке в шапке
     new_page = BasketPage(page.browser, page.url)
     new_page.should_basket_is_empty()             # Ожидаем, что в корзине нет товаров
     new_page.should_be_send_basket_is_empty()     # Ожидаем, что есть текст о том что корзина пуста

@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        config = configparser.ConfigParser()
        config.read("test.ini")         # create .ini file to store variable, ex. PASSWORD
        LINK = "http://selenium1py.pythonanywhere.com/"
        EMAIL = str(time.time()) + "@fakemail.org"
        PASSWORD = config.get("DATA", "password")

        product = LoginPage(browser, LINK)
        product.open()
        product.go_to_login_page()
        product.is_element_present(*LoginPageLocators.REGISTRATION_FORM)
        product.register_new_user(EMAIL, PASSWORD)

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        prod_page = ProductPage(browser, link)
        prod_page.open()                          # Открываем страницу товара
        prod_page.should_be_check()               # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        prod_page = ProductPage(browser, link)
        prod_page.open()
        prod_page.should_be_product_page()