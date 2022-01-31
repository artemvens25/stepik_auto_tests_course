from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    # Открываем ссылку в браузере
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем данными поля
    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys('Artem')

    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys('Vedeneev')

    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys('blabla@blabla.ru')

    # Находим кнопку загрузки файла
    us_file = browser.find_element(By.ID, 'file')

    # Открываем текущую директорию с файлами
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # Находим файл
    file_path = os.path.join(current_dir, 'blablabla')
    # Загружаем файл
    us_file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()



