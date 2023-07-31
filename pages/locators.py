from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")

    LOGIN_FORM_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")

    REGISTRATION_FORM_USERNAME =        (By.CSS_SELECTOR, "#id_registration-email.form-control")
    REGISTRATION_FORM_PASSWORD =        (By.CSS_SELECTOR, "#id_registration-password1.form-control")
    REGISTRATION_FORM_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2.form-control")

class PurchaseLocators():
    ADD_TO_PURCHASE = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    SHOW_PURCHASE =   (By.CLASS_NAME, "btn btn-default")
    NAME_STUFF =      (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    NAME_IN_BASKET =  (By.CSS_SELECTOR, ".col-sm-4 a")
    VIEW_BASKET =     (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs a.btn.btn-default")
    ELEMENT_PRICE =   (By.CSS_SELECTOR, "p.price_color")
    HAS_BEEN_ADDED =  (By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner strong")
    BASKET_PRICE =    (By.CSS_SELECTOR, ".alertinner p strong")

class BasePageLocators():
    LOGIN_LINK =         (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
