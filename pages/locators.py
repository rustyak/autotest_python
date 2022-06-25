from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    login = (By.ID, "login_form")
    register = (By.ID, "register_form")


class ProductPageLocators():
    add_to_basket = (By.CSS_SELECTOR, ".add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SECCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")