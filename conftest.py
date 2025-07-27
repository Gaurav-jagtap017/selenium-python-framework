import pytest
from selenium import webdriver
import time

@pytest.fixture
def setup():
    driver= webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    time.sleep(10)
    yield driver
    driver.quit()
