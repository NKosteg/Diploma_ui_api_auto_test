import allure
import time

from page.AuthPage import AuthPage
from page.ProjectPage import ProjectPage


@allure.suite("UI тест-кейсы")
@allure.title("Создание колонки(незавершенная попытка)")
@allure.description("Попытка создать колонку не завершена, "
                    "поскольку досоверно не определить локатор поля ввода названия колонки(при попытке определения, поле пропадает)"
                    "Добился того, что через API создается и удаляется проект и доска,"
                    "Затем уже через UI осуществляется переход к созданному через API проектуи попытка создать колонку. "
                    "P.S. Чтобы был виден результат, в этом файле и в файле ProjectPage.py оставлены sleep и print")
def test_create_task(create_and_delete_project_for_ui: str, test_data: dict, browser):
    email = test_data.get("user_email")
    password = test_data.get("user_pass")

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    project_page = ProjectPage(browser)
    print(create_and_delete_project_for_ui)
    project_page.open_project(create_and_delete_project_for_ui)
    project_page.create_column()
    time.sleep(5)
