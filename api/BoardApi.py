import requests

class BoardApi:

    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    def get_all_boards_by_org_id(self, org_id: str) -> list:
        path = "{yougile}/api-v2/boards?projectId={id}".format(yougile = self.base_url, id = org_id)
        my_headers = {"Authorization" : self.token}
        print(path)
        resp = requests.get(path, headers=my_headers)
        return resp.json().get("content")

    def create_board(self, name: str, org_id: str) -> dict:
        my_headers = {"Authorization": self.token}
        body = {
            'title': name,
            'projectId': org_id
        }
        path = "{yougile}/api-v2/boards".format(yougile = self.base_url)
        resp = requests.post(path, headers=my_headers, json=body)
        return resp.json()

    def delete_board_by_id(self, board_id: str) -> dict:
        my_headers = {"Authorization": self.token}
        body = {
            'deleted': True
        }
        path = "{yougile}/api-v2/boards/{id}".format(yougile = self.base_url, id = board_id)
        resp = requests.put(path, headers=my_headers, json=body)
        return resp.json()
