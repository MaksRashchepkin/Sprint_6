from conftest import driver
from page_object.pages.main_page import MainPage
from data import Url
import allure

class TestHeaderLogo:
    @allure.title('Клик на лого Самокат в шапке страницы открывает главную страницу Яндекс Самокат')
    def test_switch_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open_scooter_main_page()
        main_page.click_scooter_logo()
        main_page.check_switch_scooter_page()
        assert main_page.get_current_url() == Url.scooter_main_page

    @allure.title('Клик на лого Яндекс в шапке страницы открывает главную страницу Дзен')
    def test_switch_dzen_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open_scooter_main_page()
        main_page.click_yandex_logo()
        main_page.tab_switch(driver)
        main_page.check_switch_dzen_page()
        assert main_page.get_current_url() == Url.dzen_main_page
