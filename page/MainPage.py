import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


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

    @allure.step("Открыть раздел меню")
    def get_menu_section(self, num: str) -> None:
        num = int(num)
        menu_list = self.__driver.find_elements(By.CSS_SELECTOR,
                                                '.select-none.text-14.leading-4.text-panel-text-primary.whitespace-nowrap')
        my_tasks = menu_list[num]
        my_tasks.click()

    @allure.step("Проверить название в шапке окна задач")
    def read_the_name_tasks(self) -> str:
        name = self.__driver.find_element(By.CSS_SELECTOR, '.text-sm-semibold.text-panel-text-primary.flex-none.flex.items-center').text
        return name

    @allure.step("Проверить название в шапке окна ленты событий")
    def read_the_name_tape_events(self) -> str:
        name = self.__driver.find_element(By.CSS_SELECTOR,
                                          '.flex.items-center.h-56.py-12.text-sm-semibold.text-panel-text-primary').text
        return name

    @allure.step("Проверить название в шапке окна поддержки")
    def read_the_name_help(self) -> str:
        name = self.__driver.find_element(By.CSS_SELECTOR,
                                          '.h-56.py-12.px-16.flex.items-center.bg-panel-background-default').text
        return name
