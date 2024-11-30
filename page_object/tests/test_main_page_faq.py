from conftest import driver
from page_object.pages.main_page import MainPage
from data import MainPageFAQ, Url
import pytest
import allure

class TestMainPageFAQ:
    @allure.title('Проверка соответствия вопроса и ответа из выпадающего списка Вопросы о важном')
    @pytest.mark.parametrize('number, result', MainPageFAQ.answers)
    def test_main_page_faq(self, driver, number, result):
        main_page = MainPage(driver)
        main_page.open_page(Url.scooter_main_page)
        assert main_page.get_answer_text(number) == result

        # main_page.open_scooter_main_page()
        # main_page.accept_cookies()
        # main_page.find_last_question()
        # main_page.click_question(number)
        # assert main_page.get_answer(number) == answer
