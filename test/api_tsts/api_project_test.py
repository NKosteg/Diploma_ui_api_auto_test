import allure
from api.BoardApi import BoardApi

import pytest

# @pytest.mark.skip
@allure.suite("Api тест-кейсы")
@allure.feature("CREATE")
@allure.title("Создать новый проект в компании")
def test_create_project(api_client: BoardApi, test_data: dict, delete_project: dict):
    project_list_before = api_client.get_all_project()
    resp = api_client.create_project(test_data.get("user_project"))
    delete_project['project_id'] = resp.get("id")
    project_list_after = api_client.get_all_project()
    assert len(project_list_after) - len(project_list_before) == 1
    assert any(element["title"] == test_data.get("user_project") for element in project_list_after)

# @pytest.mark.skip
@allure.suite("Api тест-кейсы")
@allure.feature("UPDATE")
@allure.title("Редактировать проект")
@allure.description("Изменение названия проекта")
def test_update_project(api_client: BoardApi, create_and_delete_project: str, test_data):
    api_client.update_project(test_data.get("user_update_project"), create_and_delete_project)
    project_list_after = api_client.get_all_project()
    assert any(element["title"] == test_data.get("user_update_project") for element in project_list_after)


# @pytest.mark.skip
@allure.suite("Api тест-кейсы")
@allure.feature("DELETE")
@allure.title("Удалить проект из компании")
def test_delete_project(api_client: BoardApi, dummy_project_id: str):
    board_list_before = api_client.get_all_project()
    api_client.delete_project_by_id(dummy_project_id)
    board_list_after = api_client.get_all_project()
    assert len(board_list_before) - len(board_list_after) == 1
