from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    # Открыть сайт
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

    # Узнаем имя вкладки
    window_name = browser.window_handles[1]

    # Переходим на новую вкладку
    new_window = browser.switch_to.window(window_name)

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

    # Нажать на кнопку submit
    button2 = browser.find_element(By.CLASS_NAME, 'btn-primary')
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

