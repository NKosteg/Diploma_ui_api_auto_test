from api.BoardApi import BoardApi
from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider
import pytest

project_id = DataProvider().get("default_project_id")
url = ConfigProvider().get("api", "api_base_url")
token = DataProvider().get_token()

# @pytest.mark.skip
def test_get_boards_default_project():
    api = BoardApi(url, token)
    board_list = api.get_all_boards_by_org_id(project_id)
    assert len(board_list) == 2
    assert board_list[1]['title'] == "Сайт для зоомагазина"
