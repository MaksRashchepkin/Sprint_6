from conftest import driver
from page_object.pages.main_page import MainPage
from page_object.pages.order_page import OrderPage
from data import Users
import allure

class TestOrderPage:
    @allure.title('Проверка оформления заказа через кнопку Заказать в хедере')
    def test_create_order_header_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_scooter_main_page()
        order_page = OrderPage(driver)
        main_page.accept_cookies()
        main_page.click_header_order_button()
        order_page.create_order(Users.user_header)
        assert 'Заказ оформлен' in order_page.check_success_order()

    @allure.title('Проверка оформления заказа через кнопку Заказать в середине')
    def test_create_order_middle_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_scooter_main_page()
        order_page = OrderPage(driver)
        main_page.accept_cookies()
        main_page.click_middle_order_button()
        order_page.create_order(Users.user_middle)
        assert 'Заказ оформлен' in order_page.check_success_order()
