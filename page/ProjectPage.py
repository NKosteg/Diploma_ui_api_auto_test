import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

from configuration.ConfigProvider import ConfigProvider
import time


class ProjectPage:
    """Клас предоставляет методы для работы со страницей проекта"""

    def __init__(self, driver: WebDriver) -> None:
        self.__url = ConfigProvider().get("ui", "ui_base_url")
        self.__driver = driver

    @allure.step("Открыть страницу с проектом")
    def open_project(self, name: str):
        locator = f'[title="{name}"]'
        print(locator)
        self.__driver.find_element(By.CSS_SELECTOR, locator).click()

    @allure.step("Создать колонку")
    def create_column(self):
        list = self.__driver.find_elements(By.CSS_SELECTOR,'[role="button"]')
        button = list[3]
        button.click()
        time.sleep(5)
        name = self.__driver.find_element(By.CSS_SELECTOR,'.task-group.pt-8.bg-column-bg-gray')
        # name.send_keys('First column')
