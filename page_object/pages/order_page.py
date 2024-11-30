from page_object.locators.order_page_locators import OrderPageLocators
from page_object.pages.base_page import BasePage
import allure

class OrderPage(BasePage):
    @allure.step('Заполнить поле Имя')
    def set_name(self, name):
        self.send_keys(OrderPageLocators.name_field, name)

    @allure.step('Заполнить поле Фамилия')
    def set_last_name(self, last_name):
        self.send_keys(OrderPageLocators.last_name_field, last_name)

    @allure.step('Заполнить поле Адрес: куда привезти заказ')
    def set_address(self, address):
        self.send_keys(OrderPageLocators.address_field, address)

    @allure.step('Выбрать станцию метро')
    def set_metro(self, metro_station):
        self.click_on_element_with_wait(OrderPageLocators.metro_field)
        self.click_on_element_with_wait(OrderPageLocators.metro_station)

    @allure.step('Заполнить поле Телефон: на него позвонит курьер')
    def set_phone(self, phone):
        self.send_keys(OrderPageLocators.phone_field, phone)

    @allure.step('Нажать кнопку Далее')
    def click_next_button(self):
        self.click_on_element_with_wait(OrderPageLocators.next_button)

    @allure.step('Выбрать дату доставки')
    def set_date(self, date):
        self.click_on_element_with_wait(OrderPageLocators.date_field)
        self.click_on_element_with_wait(OrderPageLocators.date)

    @allure.step('Выбрать срок аренды')
    def set_period(self, period):
        self.click_on_element_with_wait(OrderPageLocators.period_filed)
        self.click_on_element_with_wait(OrderPageLocators.period)

    @allure.step('Выбрать цвет')
    def set_color(self, color):
        self.click_on_element_with_wait(OrderPageLocators.color)

    @allure.step('Заполнить поле Комментарий для курьера')
    def set_comment(self, comment):
        self.send_keys(OrderPageLocators.comment_field, comment)

    @allure.step('Нажать на кнопку Заказать')
    def click_order_button(self):
        self.click_on_element_with_wait(OrderPageLocators.order_button)

    @allure.step('Нажать на кнопку Да')
    def click_order_yes(self):
        self.click_on_element_with_wait(OrderPageLocators.yes_button)

    @allure.step('Проверить появления окна Заказ оформлен')
    def check_success_order(self):
        return self.find_element_with_wait(OrderPageLocators.screen_order_success)

    @allure.step('Оформить заказ')
    def create_order(self, user):
        self.set_name(user['name'])
        self.set_last_name(user['last_name'])
        self.set_address(user['address'])
        self.set_metro(OrderPageLocators.metro_station)
        self.set_phone(user['phone'])
        self.click_next_button()
        self.set_date(OrderPageLocators.date)
        self.set_period(OrderPageLocators.period)
        self.set_color(OrderPageLocators.color_black)
        self.set_comment(user['comment'])
        self.click_order_button()
        self.click_order_yes()
