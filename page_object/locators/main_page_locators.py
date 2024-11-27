from selenium.webdriver.common.by import By

class MainPageLocators:
    header_order_button = By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']" # Кнопка заказать в Хедере
    middle_order_button = By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']" # Кнопка заказать в середине
    # question_1 = By.XPATH, ".//div[@id='accordion__heading-{}']" # Вопрос
    # answer_1 = By.XPATH, ".//div[@id='accordion__panel-{}']/p" # Ответ
    question = By.XPATH, "//*[@class='my-question-locator-{}']" # Вопрос
    answer = By.XPATH, "//*[@class='my-answer-locator-{}']" # Ответ
    cookies = By.ID, "rcc-confirm-button" # Кнопка принять Куки
    last_question = By.XPATH, "(.//div[contains(@id, 'accordion__heading-')])[last()]" # Последний вопрос
    logo_scooter = By.XPATH, ".//a[@href='/']" # Лого Самокат
    logo_yandex = By.XPATH, ".//a[@href='//yandex.ru']" # Лого Яндекс
