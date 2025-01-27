from api.BoardApi import BoardApi
import allure
from testdata.DataProvider import DataProvider
import pytest


# @pytest.mark.skip
@allure.suite("Api тест-кейсы")
@allure.title("Создать новый проект в компании")
def test_create_project(api_client: BoardApi, delete_project: dict):
    project_list_before = api_client.get_all_project()
    resp = api_client.create_project("New Kosta project")
    delete_project['project_id'] = resp.get("id")
    project_list_after = api_client.get_all_project()
    assert len(project_list_after) - len(project_list_before) == 1

# @pytest.mark.skip
@allure.suite("Api тест-кейсы")
@allure.title("Удалить проект из компании")
def test_delete_project(api_client: BoardApi, dummy_project_id: str):
    board_list_before = api_client.get_all_project()
    api_client.delete_project_by_id(dummy_project_id)
    board_list_after = api_client.get_all_project()
    assert len(board_list_before) - len(board_list_after) == 1
