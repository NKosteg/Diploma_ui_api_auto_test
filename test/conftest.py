import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from api.BoardApi import BoardApi
from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider

project_id = DataProvider().get("default_project_id")
url = ConfigProvider().get("api", "api_base_url")
token = DataProvider().get_token()


@pytest.fixture
def browser() -> WebDriver:
    with allure.step("Открыть и настроить браузер"):

        timeout = ConfigProvider().get_int("ui", "timeout")
        browser_name = ConfigProvider().get("ui", "browser_name")

        if browser_name == 'chrome':
            browser = webdriver.Chrome()
        else:
            browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        browser.implicitly_wait(timeout)
        browser.maximize_window()
        yield browser
    with allure.step("Закрыть браузер"):
        browser.quit()

@pytest.fixture
def test_data():
    return DataProvider()

@pytest.fixture
def api_client() -> BoardApi:
    return BoardApi(url, token)

@pytest.fixture
def api_client_no_auth() -> BoardApi:
    return BoardApi(url, '')

@pytest.fixture
def dummy_board_id() -> str:
    api = BoardApi(url, token)
    resp = api.create_board('Board to be deleted', project_id).get('id')
    return resp

@pytest.fixture
def delete_board() -> str:
    dictionary = {'board_id' : ''}
    yield dictionary
    api = BoardApi(url, token)
    api.delete_board_by_id(dictionary.get('board_id'))
