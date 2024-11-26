from selenium.webdriver.common.by import By

class OrderPageLocators:
    name_field = [By.XPATH, ".//input[@placeholder='* Имя']"] # Поле ввода Имя
    family_field = [By.XPATH, ".//input[@placeholder='* Фамилия']"] # Поле ввода Фамилия
    address_field = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"] # Поле ввода Адрес: куда привезти заказ
    metro_field = [By.XPATH, ".//input[@placeholder='* Станция метро']"] # Поле ввода Станция метро
    metro_station = [By.XPATH, ".//input[@value='Бульвар Рокоссовского']"] # Станция метро Бульвар Рокоссовского
    phone_field = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]  # Поле ввода Телефон: на него позвонит курьер
    next_button = [By.XPATH, "button[@text='Далее']"] # Кнопка Далее
    date_field = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"] # Поле Когда привезти самокат
    date = [By.XPATH, ".//div[@class='react-datepicker__day react-datepicker__day--029 react-datepicker__day--selected']"] # Дата
    period_filed = [By.XPATH, ".//div[@class='Dropdown-placeholder']"] # Поле ввода Срок аренды
    period = [By.XPATH, ".//div[@class='Dropdown-placeholder is-selected' and text()='сутки']"] # Период сутки
    color_black = [By.XPATH, ".//label[@for='black']"] # Черный цвет
    comment_field = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]  # Поле ввода Комментарий для курьера
    order_button = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"] # Кнопка заказать
    yes_button = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']"]  # Кнопка Да
    order_success = [By.XPATH, ".//div[@class='Order_Modal__YZ-d3']/div[text()='Заказ оформлен']"]  # Экран Заказ оформлен
