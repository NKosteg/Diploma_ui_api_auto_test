import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class MainPage:
    """Клас предоставляет методы для работы со страницей профиля пользователя"""

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.__driver.current_url

    @allure.step("Открыть страницу с профилем")
    def open_profile(self) -> None:
        self.__driver.find_element(By.XPATH, '//*[@id="loggedin-container"]/div[2]/div[1]/div[7]/div[1]').click()
        self.__driver.execute_script("window.scrollBy(0, 400)")

    @allure.step("Получить имя пользователя")
    def account_name(self) -> str:
        element = self.__driver.find_element(By.CSS_SELECTOR, '[placeholder="Отображаемое имя…"]')
        name = element.get_attribute('value')
        return name
