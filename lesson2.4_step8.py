from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    # Открыть сайт браузера с перепроверкой элементов в течении 15 секунд
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку book
    button = browser.find_element(By.ID, 'book')
    money = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()


    # Вычленяем число
    x_element = browser.find_element(By.ID, 'input_value')
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
    x = x_element.text

    # Вычсляем по формуле
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)

    # Ввести число
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    # Нажать на кнопку submit
    button2 = browser.find_element(By.ID, 'solve')
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
