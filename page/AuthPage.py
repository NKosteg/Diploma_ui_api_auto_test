import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration.ConfigProvider import ConfigProvider


class AuthPage:
    """Клас предоставляет методы для работы со страницей авторизации приложения"""

    def __init__(self, driver: WebDriver) -> None:
        self.__url = ConfigProvider().get("ui", "ui_auth_url")
        self.__driver = driver

    @allure.step("Перейти на страницу авторизации")
    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Авторизоваться под {email}:{password}")
    def login_as(self, email: str, password: str):
        with allure.step(" Дождаться пока отобразится окно авторизации"):
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".login-wnd")))
            with allure.step("Заполнить поле 'E-mail:'"):
                self.__driver.find_element(By.CSS_SELECTOR, '[type="email"]').send_keys(email)
            with allure.step("Заполнить поле 'Пароль:'"):
                self.__driver.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys(password)
            with allure.step("Нажать кнопку 'Войти'"):
                self.__driver.find_element(By.CSS_SELECTOR, '[role="button"]').click()

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        # Вернем текущий url
        return self.__driver.current_url

    @allure.step("Получить название компании пользователя")
    def current_company(self) -> str:
        element = self.__driver.find_element(By.CSS_SELECTOR, ".mr-6.whitespace-nowrap.h1-semibold").text
        return element

    @allure.step("Открыть страницу с проектом")
    def open_project(self, name: str):
        locator = f"'div[title=\"{name}\"]'"
        print(locator)
        self.__driver.find_element(By.CSS_SELECTOR, 'div[title="Clark and Sons"]').click()
