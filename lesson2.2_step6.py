from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    link = 'http://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)

    select1 = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", select1)
    select1.send_keys(y)

    # Кликаем по чек боксу я робот
    input1 = browser.find_element(By.ID, "robotCheckbox")
    input1.click()

    # Кликаем по чек радиобатону
    input1 = browser.find_element(By.CSS_SELECTOR, "[for = 'robotsRule']")
    input1.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()