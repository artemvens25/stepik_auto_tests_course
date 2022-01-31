from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Вычлененеие значений
    x_element = browser.find_element(By.ID, 'num1')
    x = int(x_element.text)
    y_element = browser.find_element(By.ID, 'num2')
    y = int(y_element.text)

    # Расчет суммы полученных значений
    z = x + y

    # СПОСОБ 1
    # Раскрытие выпадающего списка с помощью select
    select1 = Select(browser.find_element(By.TAG_NAME, 'select'))

    # Выбор полученного значения
    select1.select_by_value(str(z))
    # select1.select_by_visible_text(str(z))

    # Клик по кнопке submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()