from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

try:

    sum1 = int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text)

    select = Select(browser.find_element(By.CSS_SELECTOR, "select"))
    select.select_by_value(str(sum1))

    button = browser.find_element(By.TAG_NAME, ".btn").click()


except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:

    time.sleep(10)

    browser.close()
    browser.quit()