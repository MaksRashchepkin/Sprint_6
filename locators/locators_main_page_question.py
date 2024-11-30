from selenium.webdriver.common.by import By

class MainPageLocators:
    question = (By.XPATH, "//*[@id='accordion__heading-{}']")
    answer = (By.XPATH, "//*[@id='accordion__panel-{}']")
    last_question = (By.XPATH, "//*[@id='accordion__heading-7']")
