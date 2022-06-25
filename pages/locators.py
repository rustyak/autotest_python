from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    login = (By.ID, "login_form")
    register = (By.ID, "register_form")


class ProductPageLocators():
    add_to_basket = (By.CSS_SELECTOR, ".add-to-basket")
