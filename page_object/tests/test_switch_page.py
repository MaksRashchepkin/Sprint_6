from conftest import driver
from page_object.pages.main_page import MainPage
from page_object.pages.switch_page import SwitchPage
from data import Url
import allure

class TestHeaderLogo:
    @allure.title('Клик на лого Самокат в шапке страницы открывает главную страницу Яндекс Самокат')
    def test_switch_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open_scooter_main_page()
        switch_page = SwitchPage(driver)
        switch_page.click_scooter_logo()
        switch_page.check_switch_scooter_page()
        assert main_page.get_current_url() == Url.scooter_main_page

    @allure.title('Клик на лого Яндекс в шапке страницы открывает главную страницу Дзен')
    def test_switch_dzen_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open_scooter_main_page()
        switch_page = SwitchPage(driver)
        switch_page.click_yandex_logo()
        switch_page.check_switch_dzen_page()
        assert main_page.get_current_url() == Url.dzen_main_page
