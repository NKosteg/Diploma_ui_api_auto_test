from api.BoardApi import BoardApi
from testdata.DataProvider import DataProvider
import pytest
import allure

project_id = DataProvider().get("default_project_id")

# @pytest.mark.skip
@allure.suite("Api тест-кейсы")
@allure.feature("READ")
@allure.title("Получение списка досок из проекта по умолчанию")
@allure.description("Поскольку в сервисе Yougile, после создания и регистрации компании уже есть пример проекта,"
                    "можно получить список досок из проекта по умолчанию")
def test_get_boards_default_project(api_client: BoardApi):
    board_list = api_client.get_all_boards_by_org_id(project_id)
    assert len(board_list) == 2
    assert board_list[1]['title'] == "Сайт для зоомагазина"


# @pytest.mark.skip
@allure.suite("Api тест-кейсы")
@allure.feature("CREATE")
@allure.title("Создать новую доску на проекте по умолчанию")
@allure.description("Использование в тестах id проекта по умолчанию, после  создания и регистрации компании в сервисе Yougile")
def test_create_board(api_client: BoardApi, delete_board: dict):
    board_list_before = api_client.get_all_boards_by_org_id(project_id)
    resp =api_client.create_board("Test board", project_id)
    delete_board['board_id'] = resp.get("id")
    board_list_after = api_client.get_all_boards_by_org_id(project_id)
    assert len(board_list_after) - len(board_list_before) == 1

# @pytest.mark.skip
@allure.suite("Api тест-кейсы")
@allure.feature("DELETE")
@allure.title("Удалить доску с проекта по умолчанию")
@allure.description("Использование в тестах id проекта по умолчанию, после регистрации и создания компании в сервисе Yougile")
def test_delete_board(api_client: BoardApi, dummy_board_id: str):
    board_list_before = api_client.get_all_boards_by_org_id(project_id)
    api_client.delete_board_by_id(dummy_board_id)
    board_list_after = api_client.get_all_boards_by_org_id(project_id)
    assert len(board_list_before) - len(board_list_after) == 1

# @pytest.mark.skip
@allure.suite("Api тест-кейсы")
@allure.feature("CREATE")
@allure.title("Создать новую доску на новом проекте")
@allure.description("Создание новой доски, в созданом для этого проекте, с его последующим удалением")
def test_create_board1(api_client: BoardApi, create_and_delete_project: str):
    board_list_before = api_client.get_all_boards_by_org_id(create_and_delete_project)
    api_client.create_board("Test fifth board", create_and_delete_project)
    board_list_after = api_client.get_all_boards_by_org_id(create_and_delete_project)
    assert len(board_list_after) - len(board_list_before) == 1

# @pytest.mark.skip
@allure.suite("Api тест-кейсы")
@allure.feature("DELETE")
@allure.title("Удалить доску с нового проекта ")
@allure.description("Создание двух досок и последующее удаление последней доски из проекта, "
                    "поскольку по требованиям нельзя удалять единственную доску из проекта, "
                    "в созданном для этого проекте, с его последующим удалением")
def test_delete_board1(api_client: BoardApi, create_and_delete_project: str, dummy_two_board_id: str):
    board_list_before = api_client.get_all_boards_by_org_id(create_and_delete_project)
    api_client.delete_board_by_id(dummy_two_board_id)
    board_list_after = api_client.get_all_boards_by_org_id(create_and_delete_project)
    assert len(board_list_before) - len(board_list_after) == 1