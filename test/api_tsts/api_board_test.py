from api.BoardApi import BoardApi
import pytest

project_id = "1c2066f3-5040-4275-b20c-f9fc6b9fb1b8"

# @pytest.mark.skip
def test_get_boards(api_client: BoardApi):
    board_list = api_client.get_all_boards_by_org_id(project_id)
    assert len(board_list) >= 2
# @pytest.mark.skip
def test_create_board(api_client: BoardApi, delete_board: dict):
    board_list_before = api_client.get_all_boards_by_org_id(project_id)

    resp =api_client.create_board("Test board", project_id)
    delete_board['board_id'] = resp.get("id")

    board_list_after = api_client.get_all_boards_by_org_id(project_id)

    assert len(board_list_after) - len(board_list_before) == 1
# @pytest.mark.skip
def test_delete_board(api_client: BoardApi, dummy_board_id: str):
    board_list_before = api_client.get_all_boards_by_org_id(project_id)
    api_client.delete_board_by_id(dummy_board_id)
    board_list_after = api_client.get_all_boards_by_org_id(project_id)
    assert len(board_list_before) - len(board_list_after) == 1


