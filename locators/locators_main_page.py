from selenium.webdriver.common.by import By

class MainPageLocators:
    question = (By.XPATH, "//*[@id='accordion__heading-{}']") # Вопрос
    answer = (By.XPATH, "//*[@id='accordion__panel-{}']") # Ответ
    last_question = (By.XPATH, "//*[@id='accordion__heading-7']") # Последний вопрос

    header_order_button = By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"  # Кнопка заказать в хедере
    page_order_button = By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"  # Кнопка заказать в середине страницы

