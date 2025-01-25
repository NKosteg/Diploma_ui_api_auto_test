import allure
from page.AuthPage import AuthPage
from page.MainPage import MainPage

import pytest

# @pytest.mark.skip
def test_auth(browser, test_data):
    my_company = test_data.get("user_company")
    my_name = test_data.get("user_name")
    email = test_data.get("user_email")
    password = test_data.get("user_pass")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)
    user_company = auth_page.current_company()

    main_page = MainPage(browser)
    main_page.open_profile()
    user_name = main_page.account_name()

    with allure.step("Проверить, что current_url заканчивается на '/team/settings-account'"):
        assert main_page.get_current_url().endswith('/team/settings-account')
    with allure.step("Проверить, что название компании 'Potok_101'"):
        assert user_company == my_company
    with allure.step("Проверить, что имя пользователя 'Konstantin Nikolaev'"):
        assert user_name == my_name
