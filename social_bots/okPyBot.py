# from ok_api import OkApi
from json import load
from pathlib import Path
from requests import Session, post
from hashlib import md5

class Main:
    ok_api_url = "https://api.ok.ru/fb.do?"

    def __init__(self, method, params = ""):
        with open(Path().joinpath("src", "ok.json")) as f:
            data = load(f)

        self.access_token = data["access_token"]
        self.application_key = data["public_key"]
        self.session_secret_key = data["session_secret_key"]
        self.params = "".join([
            "{}={}".format(key, params[key]) for key in sorted(params.keys())
        ]) if params != "" else ""
        self.method = method
        self.sig = md5(
            f"application_key={self.application_key}{self.params}method={self.method}{self.session_secret_key}".encode("utf-8")).hexdigest().lower()
        self.api_req = "&".join([
            f"application_key={self.application_key}",
            self.params,
            f"method={self.method}",
            f"sig={self.sig}",
            f"access_token={self.access_token}",
        ])
        
        print(self.api_req)
        # self.datas = {
        #     "application_key": self.application_key,
        #     "access_token": self.access_token,
        #     "sig": self.sig,
        #     "method": self.method,
        # }

    @property
    def post(self):
        return post("".join([
            self.ok_api_url,
            self.api_req,
        ])).json()


if __name__ == "__main__":
    c = Main("mediatopic.post", {
        "type": "GROUP_THEME",
        "gid": 60763350106154,
        "attachment": {
            "media": [
                {
                    "type": "text",
                    "text": "test"
                },
            ],
            "publishAt": "2021-04-30 15:35:13",
            "onBehalfGroup": "false",
            "disableComments": "true"
        },
    })
    # c = Main("users.getCurrentUser")
    print(c.post)
