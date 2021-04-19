# from ok_api import OkApi
from json import load
from pathlib import Path
from requests import Session, post, get

class Activity():
    basic_url = "https://api.ok.ru/fb.do?method="

    def __init__(self):
        with open(Path().joinpath("src", "ok.json")) as f:
            self.data = load(f)

    @property
    def http(self):
        return Session()

    @property
    def __get_session_secret_key(self):
        print()