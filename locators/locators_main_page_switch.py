from selenium.webdriver.common.by import By

class MainPageSwitchLocators:
    logo_header_scooter = (By.XPATH, ".//a[@href='/']") # Лого Самокат
    logo_header_yandex = (By.XPATH, ".//a[@href='//yandex.ru']") # Лого Яндекс