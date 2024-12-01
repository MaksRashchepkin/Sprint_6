from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://qa-scooter.praktikum-services.ru/')
    driver.find_element(By.ID, "rcc-confirm-button").click()
    yield driver
    driver.quit()
