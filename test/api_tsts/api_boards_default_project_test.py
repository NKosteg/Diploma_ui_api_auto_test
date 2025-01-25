from api.BoardApi import BoardApi
import pytest

project_id = "1c2066f3-5040-4275-b20c-f9fc6b9fb1b8"
url = 'https://yougile.com'
token = "Bearer 0WVzxD4Kvdz07W9iwqZbXEaHgqbIX-q5OHYhK5gvcFOUQD1S6FfqlOc9pd0sFhWD"

@pytest.mark.skip
def test_get_boards_default_project():
    api = BoardApi(url, token)
    board_list = api.get_all_boards_by_org_id(project_id)
    assert len(board_list) == 2
    assert board_list[1]['title'] == "Сайт для зоомагазина"
