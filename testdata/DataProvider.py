import json

my_file = open('test_data.json')
global_data = json.load(my_file)

class DataProvider:

    def __init__(self) -> None:
        self.data = global_data

    def get_token(self) -> str:
        return self.data.get("user_token")

    def get(self, prop) -> str:
        return self.data.get(prop)

    def get_int(self, prop: str) -> int:
        val =  self.data.get(prop)
        return int(val)
