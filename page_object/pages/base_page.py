from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def get_text(self, locator):
        return self.find_element(locator).text

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def cross_url(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))

    def tab_switch(self, driver):
        self.driver.switch_to.window(driver.window_handles[1])

    def get_current_url(self):
        return self.driver.current_url

    def wait_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    def open_page(self, url):
        self.driver.get(url)

    def format_locators(self, locator_1, number):
        method, locator = locator_1
        locator = locator.format(number)
        return (method, locator)
