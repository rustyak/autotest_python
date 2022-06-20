from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=chrome_options)

    def go_to_link():
        return browser.get(link)

    def click_to_button():
        button = browser.find_element(By.TAG_NAME, 'button')
        return button.click()

    def find_new_window():
        new_window = browser.window_handles[1]
        return new_window

    def switch_to_window(new_window):
        return browser.switch_to.window(new_window)

    def find_x():
        x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
        x = x_element.text
        return x

    def calc(x):
        y = str(math.log(abs(12 * math.sin(int(x)))))
        return y

    def insert_answer(y):
        answer = browser.find_element(By.XPATH, "//input[@id='answer']")
        return answer.send_keys(y)

    def click_to_submit():
        submit = browser.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        return submit.click()

    step1 = go_to_link()
    step2 = click_to_button()
    step3_1 = find_new_window()
    step3_2 = switch_to_window(step3_1)
    step4_1 = find_x()
    step4_2 = calc(step4_1)
    step4_3 = insert_answer(step4_2)
    step4_4 = click_to_submit()

finally:
    time.sleep(10)
    browser.quit()