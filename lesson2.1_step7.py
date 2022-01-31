from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Высчитываем значения уравнения
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)

    # Вставляем значение в строку ответа
    input0 = browser.find_element(By.ID, "answer")
    input0.send_keys(y)

    # Кликаем по чек боксу я робот
    input1 = browser.find_element(By.ID, "robotCheckbox")
    input1.click()

    # Кликаем по чек радиобатону
    input1 = browser.find_element(By.ID, "robotsRule")
    input1.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()