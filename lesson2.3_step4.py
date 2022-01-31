from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    # Открываем ссылку в браузере
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать по кнопке на странице
    button = browser.find_element(By.CLASS_NAME, 'btn-primary')
    button.click()

    # Принять конфирм
    confirm = browser.switch_to.alert
    confirm.accept()

    # Вычленяем число
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text

    # Вычсляем по формуле
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)

    # Ввести число
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    # Нажать по кнопке submit
    button = browser.find_element(By.CLASS_NAME, 'btn-primary')
    button.click()

finally:
    # Ожидание
    time.sleep(15)
    # Закрытие браузера
    browser.quit()
