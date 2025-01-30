import allure
import requests


class BoardApi:
    """Клас предоставляет методы для работы с сервером приложеня"""

    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    @allure.step("Получить список проектов")
    def get_all_project(self) -> list:
        my_headers = {"Authorization": self.token}
        path = "{yougile}/api-v2/projects".format(yougile=self.base_url)
        resp = requests.get(path, headers=my_headers)
        return resp.json().get("content")

    @allure.step("Создать проект  {name}")
    def create_project(self, name: str, user: dict = None) -> dict:
        my_headers = {"Authorization": self.token}
        body = {
            'title': name,
            'users': user
        }
        path = "{yougile}/api-v2/projects".format(yougile=self.base_url)
        resp = requests.post(path, headers=my_headers, json=body)
        return resp.json()

    @allure.step("Получить название проекта с id {project_id}")
    def get_project_by_id(self, project_id) -> dict:
        my_headers = {"Authorization": self.token}
        path = "{yougile}/api-v2/projects/{id}".format(yougile=self.base_url, id=project_id)
        resp = requests.get(path, headers=my_headers)
        return resp.json()

    @allure.step("Изменение названия проекта с id {project_id} на {new_name}")
    def update_project(self, new_name, project_id) -> dict:
        my_headers = {"Authorization": self.token}
        body = {
            'title': new_name
        }
        path = "{yougile}/api-v2/projects/{id}".format(yougile=self.base_url, id=project_id)
        resp = requests.put(path, headers=my_headers, json=body)
        return resp.json()

    @allure.step("Удалить проект с id {project_id}")
    def delete_project_by_id(self, project_id: str) -> dict:
        my_headers = {"Authorization": self.token}
        body = {
            'deleted': True
        }
        path = "{yougile}/api-v2/projects/{id}".format(yougile=self.base_url, id=project_id)
        resp = requests.put(path, headers=my_headers, json=body)
        return resp.json()

    @allure.step("Получить список досок проекта {org_id}")
    def get_all_boards_by_org_id(self, org_id: str) -> list:
        path = "{yougile}/api-v2/boards?projectId={id}".format(yougile=self.base_url, id=org_id)
        my_headers = {"Authorization": self.token}
        resp = requests.get(path, headers=my_headers)
        return resp.json().get("content")

    @allure.step("Создать доску {name} на проекте {org_id}")
    def create_board(self, name: str, org_id: str) -> dict:
        my_headers = {"Authorization": self.token}
        body = {
            'title': name,
            'projectId': org_id
        }
        path = "{yougile}/api-v2/boards".format(yougile=self.base_url)
        resp = requests.post(path, headers=my_headers, json=body)
        return resp.json()

    @allure.step("Изменить название на {new_name} доски {board_id}")
    def update_board_by_id(self, board_id: str, new_name: str) -> str:
        my_headers = {"Authorization": self.token}
        body = {
            'title': new_name
        }
        path = "{yougile}/api-v2/boards/{id}".format(yougile=self.base_url, id=board_id)
        resp = requests.put(path, headers=my_headers, json=body)
        return resp.json().get("id")

    @allure.step("Получить доску {board_id}")
    def get_board_by_id(self, board_id: str) -> dict:
        my_headers = {"Authorization": self.token}
        path = "{yougile}/api-v2/boards/{id}".format(yougile=self.base_url, id=board_id)
        resp = requests.get(path, headers=my_headers)
        return resp.json()

    @allure.step("Удалить доску {board_id}")
    def delete_board_by_id(self, board_id: str) -> dict:
        my_headers = {"Authorization": self.token}
        body = {
            'deleted': True
        }
        path = "{yougile}/api-v2/boards/{id}".format(yougile=self.base_url, id=board_id)
        resp = requests.put(path, headers=my_headers, json=body)
        return resp.json()
