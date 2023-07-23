from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")

    LOGIN_FORM_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")

    REGISTRATION_FORM_USERNAME= (By.CSS_SELECTOR, "#id_registration-email.form-control")
    REGISTRATION_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1.form-control")
    REGISTRATION_FORM_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2.form-control")