from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    log_in = (By.CSS_SELECTOR, "#login_link")
    sign_up = (By.CSS_SELECTOR, "#login_link")

