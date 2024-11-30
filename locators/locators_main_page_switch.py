from selenium.webdriver.common.by import By

class MainPageSwitchLocators:
    button_header_scooter = (By.XPATH, ".//a[@href='/']")
    button_header_yandex = (By.XPATH, ".//a[@href='//yandex.ru']")
    #button_look_at_status = (By.XPATH, "//*[text() = 'Посмотреть статус']")
    #search_yandex_field = (By.XPATH, "//a[contains(@class, 'dzen-layout--desktop-base-header__logo')]")