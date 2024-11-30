import pytest
import allure
from conftest import driver
from pages.main_page_question import MainPageQuestion
from data import Url, MainPageAnswers

class TestQuestionText:
    @allure.title('Проверка соответствия вопроса и ответа из выпадающего списка Вопросы о важном')
    @pytest.mark.parametrize('number, result', MainPageAnswers.answers)
    def test_main_page_question(self, driver, number, result):
        main_page = MainPageQuestion(driver)
        main_page.enter_the_page(Url.scooter_main_page)
        assert  main_page.get_text_assert(number) == result