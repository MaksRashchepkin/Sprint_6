from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Методы для теста Вопросы о важном
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def get_text_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    def format_locators(self, locator_1, number):
        method, locator = locator_1 # "//*[@class='my-question-locator-{}']"
        locator = locator.format(number) # "//*[@class='my-question-locator-1']"
        return (method, locator)

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    # Другие методы
    def send_keys(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

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



