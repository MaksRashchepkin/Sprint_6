import allure
import pytest
from conftest import driver
from locators.locators_page_order_scroller import PageOrderLocators
from pages.page_order_scooter import OrderScooterPage
from pages.main_page import MainPage
from data import UserOne, UserTwo

class TestPageOrder:
    @allure.title('Проверка оформления заказа через кнопку "Заказать" в хедере')
    @pytest.mark.parametrize('name, surname, address, metro, telephone, when_scooter, the_rental_period, check_box_colour, comment', UserOne.user)
    def test_order_header_button(self, driver, name, surname, address, metro, telephone, when_scooter, the_rental_period, check_box_colour, comment):
        main_page = MainPage(driver)
        main_page.click_header_order_button()
        order_page = OrderScooterPage(driver)
        order_page.enter_name(name)
        order_page.enter_surname(surname)
        order_page.enter_address(address)
        order_page.enter_metro(metro)
        order_page.enter_telephone(telephone)
        order_page.click_on_button_enter_first_page_order()
        order_page.enter_when_scooter(when_scooter)
        order_page.enter_when_check_box_colour(check_box_colour)
        order_page.enter_the_rental_period(the_rental_period)
        order_page.enter_comment(comment)
        order_page.click_on_button_order()
        order_page.check_screen_want_set_order()
        order_page.click_on_button_yes_or_not()
        order_page.check_screen_set_order_complete()
        assert driver.find_element(*PageOrderLocators.screen_order_complete).is_displayed()

    @allure.title('Проверка оформления заказа через кнопку "Заказать" в середине страницы')
    @pytest.mark.parametrize('name, surname, address, metro, telephone, when_scooter, the_rental_period, check_box_colour, comment', UserTwo.user)
    def test_order_middle_button(self, driver, name, surname, address, metro, telephone, when_scooter, the_rental_period, check_box_colour, comment):
        main_page = MainPage(driver)
        main_page.click_middle_order_button()
        order_page = OrderScooterPage(driver)
        order_page.enter_name(name)
        order_page.enter_surname(surname)
        order_page.enter_address(address)
        order_page.enter_metro(metro)
        order_page.enter_telephone(telephone)
        order_page.click_on_button_enter_first_page_order()
        order_page.enter_when_scooter(when_scooter)
        order_page.enter_when_check_box_colour(check_box_colour)
        order_page.enter_the_rental_period(the_rental_period)
        order_page.enter_comment(comment)
        order_page.click_on_button_order()
        order_page.check_screen_want_set_order()
        order_page.click_on_button_yes_or_not()
        order_page.check_screen_set_order_complete()
        assert driver.find_element(*PageOrderLocators.screen_order_complete).is_displayed()
