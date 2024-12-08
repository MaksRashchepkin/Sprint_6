from selenium import webdriver
import pytest
from data import Url
from locators.locators_main_page import MainPageLocators
import time

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    time.sleep(1)
    yield driver
    driver.quit()

@pytest.fixture
def cookies(driver):
    driver.get(Url.scooter_main_page)
    driver.find_element(*MainPageLocators.cookies_button).click()
    time.sleep(1)
    return cookies
