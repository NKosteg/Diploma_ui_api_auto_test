from api.BoardApi import BoardApi
from testdata.DataProvider import DataProvider
import allure

project_id = DataProvider().get("default_project_id")


@allure.suite("Api тест-кейсы")
@allure.feature("READ")
@allure.title("Получение списка досок из проекта по умолчанию")
@allure.description("Поскольку в сервисе Yougile, после создания и регистрации компании уже есть пример проекта,"
                    "можно получить список досок из проекта по умолчанию")
def test_get_boards_default_project(api_client: BoardApi):
    board_list = api_client.get_all_boards_by_org_id(project_id)
    assert len(board_list) == 2
    assert board_list[1]['title'] == "Сайт для зоомагазина"


@allure.suite("Api тест-кейсы")
@allure.feature("CREATE")
@allure.title("Создать новую доску на проекте по умолчанию")
@allure.description("Использование в тестах id проекта по умолчанию, после  создания и регистрации компании в сервисе Yougile")
def test_create_board(api_client: BoardApi, test_data: dict, delete_board: dict):
    board_list_before = api_client.get_all_boards_by_org_id(project_id)
    resp = api_client.create_board(test_data.get("user_board"), project_id)
    delete_board['board_id'] = resp.get("id")
    board_list_after = api_client.get_all_boards_by_org_id(project_id)
    assert len(board_list_after) - len(board_list_before) == 1
    assert any(element["title"] == test_data.get("user_board") for element in board_list_after)


@allure.suite("Api тест-кейсы")
@allure.feature("DELETE")
@allure.title("Удалить доску с проекта по умолчанию")
@allure.description("Использование в тестах id проекта по умолчанию, после регистрации и создания компании в сервисе Yougile")
def test_delete_board(api_client: BoardApi, dummy_board_id: str):
    board_list_before = api_client.get_all_boards_by_org_id(project_id)
    api_client.delete_board_by_id(dummy_board_id)
    board_list_after = api_client.get_all_boards_by_org_id(project_id)
    assert len(board_list_before) - len(board_list_after) == 1


@allure.suite("Api тест-кейсы")
@allure.feature("CREATE")
@allure.title("Создать новую доску на новом проекте")
@allure.description("Создание новой доски, в созданом для этого проекте, с его последующим удалением")
def test_create_board_new_project(api_client: BoardApi, test_data: dict, create_and_delete_project: str):
    board_list_before = api_client.get_all_boards_by_org_id(create_and_delete_project)
    api_client.create_board(test_data.get("user_board"), create_and_delete_project)
    board_list_after = api_client.get_all_boards_by_org_id(create_and_delete_project)
    assert len(board_list_after) - len(board_list_before) == 1
    assert any(element["title"] == "Test Kosta board" for element in board_list_after)


@allure.suite("Api тест-кейсы")
@allure.feature("UPDATE")
@allure.title("Редактирование доски на новом проекте")
@allure.description("Редактирование названия новой доски, в созданом для этого проекте, с его последующим удалением")
def test_update_board_new_project(api_client: BoardApi, test_data: dict, create_and_delete_project: str, dummy_update_board_id: str):
    update_board_id = api_client.update_board_by_id(dummy_update_board_id, test_data.get("user_update_board"))
    body = api_client.get_board_by_id(update_board_id)
    assert body.get("title") == test_data.get("user_update_board")


@allure.suite("Api тест-кейсы")
@allure.feature("DELETE")
@allure.title("Удалить доску с нового проекта ")
@allure.description("Создание двух досок и последующее удаление последней доски из проекта, "
                    "поскольку по требованиям нельзя удалять единственную доску из проекта, "
                    "в созданном для этого проекте, с его последующим удалением")
def test_delete_board_new_project(api_client: BoardApi, create_and_delete_project: str, dummy_two_board_id: str):
    board_list_before = api_client.get_all_boards_by_org_id(create_and_delete_project)
    api_client.delete_board_by_id(dummy_two_board_id)
    board_list_after = api_client.get_all_boards_by_org_id(create_and_delete_project)
    assert len(board_list_before) - len(board_list_after) == 1
