# Тестовый запуск

from selenium import webdriver
import time

# инициализируем драйвер браузера
driver = webdriver.Firefox()
driver.maximize_window()

# сделаем паузу
time.sleep(3)

# закроем браузер
driver.quit()
