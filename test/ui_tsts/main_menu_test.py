import allure

from page.AuthPage import AuthPage
from page.MainPage import MainPage


@allure.suite("UI тест-кейсы")
@allure.feature("READ")
@allure.title("Переход к окну мои задачи")
def test_my_tasks_menu(browser, test_data: dict):
    email = test_data.get("user_email")
    password = test_data.get("user_pass")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.get_menu_section(0)
    name_menu = main_page.read_the_name_tasks()
    with allure.step("Проверить что название соответствует окну"):
        assert name_menu == 'Мои задачи'


@allure.suite("UI тест-кейсы")
@allure.feature("READ")
@allure.title("Переход к окну чужие задачи")
def test_strangers_tasks_menu(browser, test_data: dict):
    email = test_data.get("user_email")
    password = test_data.get("user_pass")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.get_menu_section('1')
    name_menu = main_page.read_the_name_tasks()
    with allure.step("Проверить что название соответствует окну"):
        assert name_menu == 'Чужие задачи'


@allure.suite("UI тест-кейсы")
@allure.feature("READ")
@allure.title("Переход к окну ленты событий")
def test_events_menu(browser, test_data: dict):
    email = test_data.get("user_email")
    password = test_data.get("user_pass")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.get_menu_section('4')
    name_menu = main_page.read_the_name_tape_events()
    with allure.step("Проверить что название соответствует окну"):
        assert name_menu == 'Лента событий'


@allure.suite("UI тест-кейсы")
@allure.feature("READ")
@allure.title("Переход к окну поддержки")
def test_help_menu(browser, test_data: dict):
    email = test_data.get("user_email")
    password = test_data.get("user_pass")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.get_menu_section('7')
    name_menu = main_page.read_the_name_help()
    with allure.step("Проверить что название соответствует окну"):
        assert name_menu == 'Помощь по YouGile, новости'
