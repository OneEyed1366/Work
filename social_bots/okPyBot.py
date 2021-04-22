# from ok_api import OkApi
from json import load
from pathlib import Path
from hashlib import md5
from requests import Session, post, get
from ok_api import OkApi

def main():
    with open(Path().joinpath("src", "ok.json")) as f:
        data = load(f)

    ok = OkApi(
        access_token = data["access_token"],
        application_key = data["public_key"],
        application_secret_key = data["secret_key"],
    )

    response = ok.friends.get()
    print(response.json())

if __name__ == "__main__":
    main()

# class Activity:
#     basic_url = "https://api.ok.ru/fb.do"

#     def __init__(self):
        # with open(Path().joinpath("src", "ok.json")) as f:
        #     self.data = load(f)

#         self.__access_token = self.data["access_token"]
#         self.__application_key = self.data["public_key"]
#         self.__application_secret_key = self.data["secret_key"]
#         self.__methods = None

#     @property
#     def http(self):
#         return Session()

#     @property
#     def __get_session_secret_key(self):
#         return md5(f"{self.__access_token}{self.__application_secret_key}".encode('utf-8')).hexdigest().lower()

#     def __signature(self, params):
#         params = "".join([f"{key}={params[key]}" for key in sorted(params.keys())])
        
#         return md5(f"{params}{self.__get_session_secret_key}".encode("utf-8")).hexdigest().lower()

#     # def __getattr__(self, item):
#     #     ok_api = Activity()
#     #     ok_api.__methods = self.__methods + '.' + item if self.__methods else item


# print(Activity.__signature('test'))
