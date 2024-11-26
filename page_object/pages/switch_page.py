from page_object.locators.switch_page_locators import SwitchPageLocators
from page_object.pages.base_page import BasePage
from data import Url
import allure


class SwitchPage(BasePage):
    @allure.step('Нажать на лого Яндекс')
    def click_yandex_logo(self):
        self.click_on_element(SwitchPageLocators.logo_yandex)

    @allure.step('Нажать на лого Самокат')
    def click_scooter_logo(self):
        self.click_on_element(SwitchPageLocators.logo_scooter)

    @allure.step('Проверить URL Яндекс Самокат')
    def check_switch_scooter_page(self):
        self.cross_url(Url.scooter_main_page)

    @allure.step('Проверить URL Дзен')
    def check_switch_dzen_page(self):
        self.cross_url(Url.dzen_main_page)
