import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from pages.home_page import MxHomePage


options = Options()


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()


@pytest.fixture
def home_page(driver):
    yield MxHomePage(driver)



