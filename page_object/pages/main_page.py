from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.base_page import BasePage
from data import Url
import allure

class MainPage(BasePage):
    @allure.step('Нажать на кнопку Заказать в хедере')
    def click_header_order_button(self):
        self.click_on_element(MainPageLocators.header_order_button)

    @allure.step('Нажать на кнопку Заказать в футере')
    def click_middle_order_button(self):
        self.click_on_element(MainPageLocators.middle_order_button)

    @allure.step('Нажать на вопрос')
    def click_question(self, number):
        method, locator = MainPageLocators.question
        locator = locator.format(number)
        return self.click_on_element((method, locator))

    # @allure.step('Получить текст ответа на вопрос')
    # def get_answer(self, number):
        # method, locator = MainPageLocators.answer
        # locator = locator.format(number)
        # return self.get_text((method, locator))

    @allure.step('Получить текст ответа на вопрос')
    def get_answer_text(self, number):
        locator_q_formatted = self.format_locators(MainPageLocators.question, number)
        locator_a_formatted = self.format_locators(MainPageLocators.answer, number)
        self.click_on_element(locator_q_formatted)
        return self.get_text(locator_a_formatted)

    @allure.step('Открыть главную страницу Яндекс Самокат')
    def open_scooter_main_page(self):
        self.open_page(Url.scooter_main_page)

    @allure.step('Принять куки')
    def accept_cookies(self):
        self.wait_element(MainPageLocators.cookies)
        self.click_on_element(MainPageLocators.cookies)

    @allure.step('Найти последний вопрос')
    def find_last_question(self):
        self.find_element(MainPageLocators.last_question)

    @allure.step('Нажать на лого Яндекс')
    def click_yandex_logo(self):
        self.click_on_element(MainPageLocators.logo_yandex)

    @allure.step('Нажать на лого Самокат')
    def click_scooter_logo(self):
        self.click_on_element(MainPageLocators.logo_scooter)

    @allure.step('Проверить URL Яндекс Самокат')
    def check_switch_scooter_page(self):
        self.cross_url(Url.scooter_main_page)

    @allure.step('Проверить URL Дзен')
    def check_switch_dzen_page(self):
        self.cross_url(Url.dzen_main_page)



