from locators.locators_main_page_question import MainPageLocators
from pages.base_page import BasePage
import allure

class MainPageQuestion(BasePage):
    @allure.step('Получить текст ответа на вопрос')
    def get_text_assert(self, number):
        locator_question_to_click_formated = self.format_locators(MainPageLocators.question, number)
        locator_question_text_formated = self.format_locators(MainPageLocators.answer, number)
        self.skroll_to_element(MainPageLocators.last_question)
        self.click_on_element(locator_question_to_click_formated)
        return self.get_text(locator_question_text_formated)