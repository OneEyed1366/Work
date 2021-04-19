import os, vk_api
from re import match
from requests import Session, auth, get
from Alarmer import alarm
from json import load, dump
from datetime import datetime
from pathlib import Path
from sys import argv, exit
from time import sleep
from random import randint

users = {
    "work": {
        "login": "79204549507",
        "password": "268rfvhu",
        "user_id": 427250420,
        "app_id": "7754939",
        "acc_token": "37e6a79e8086cb4b2aa95973a4d4dc2c28e615684c262cab7b3a1e7be012e9993cab41ba854c39808633c"
    }
}


def search(path):
    if os.path.exists(path):
        return path
    elif os.path.exists(str(path).replace('й', 'й').replace('ё', 'ё')):
        return str(path).replace('й', 'й').replace('ё', 'ё')
    elif os.path.exists(str(path).replace('й', 'й')):
        return str(path).replace('й', 'й')
    elif os.path.exists(str(path).replace('ё', 'ё')):
        return str(path).replace('ё', 'ё')
    elif os.path.exists(str(path).replace('_', '?')):
        return str(path).replace('_', '?')
    elif os.path.exists(str(path).replace('?', '_')):
        return str(path).replace('?', '_')


if os.sys.platform == 'ios':
    os.chdir(
        os.path.join(
            '/private',
            'var',
            'mobile',
            'Library',
            'Mobile Documents',
            'iCloud~is~workflow~my~workflows',
            'Documents'
        )
    )
elif os.sys.platform == 'win32':
    os.chdir(
        os.path.join(
            'C:\\',
            'Users',
            'proka',
            'iCloudDrive',
            'iCloud~is~workflow~my~workflows'
        )
    )

if not os.path.exists(os.path.join(
    "Данные для работы",
    "Боты",
    "События",
    os.path.basename(__file__)
)):
    os.mkdir(
        os.path.join(
            "Данные для работы",
            "Боты",
            "События",
            os.path.basename(__file__)
        ))

with open(
        os.path.join(
            "Данные для работы",
            "Боты",
            "События",
            os.path.basename(__file__),
            "Данные.json"
        ), "w+", encoding="utf-8") as f:
    dump({
        "path": os.path.abspath(__file__),
        "last_start": datetime.today().ctime()
    }, f)

with open(
    Path().joinpath("Данные для работы", "Социалочка", "Боты.txt"),
    "r+",
    encoding="utf-8"
) as f:
    bots = f.readlines()

with open(
    Path().joinpath("Данные для работы", "Социалочка", "proxy.json"),
    "r+",
    encoding="utf-8"
) as f:
    proxies = load(f)

# combine = [text.replace("\n", "").split(":")]


my_user = users["work"]["login"]
my_password = users["work"]["password"]
my_user_id = users["work"]["user_id"]
my_app_id = users["work"]["app_id"]
my_app_token = users["work"]["acc_token"]

def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True

    return key, remember_device


class Bots_activity():
    scopes = "WALL, OFFLINE, GROUPS, STATS"
    respond_text = os.path.basename(__file__)
    session = Session()
    # link_get_token = "https://oauth.vk.com/authorize?client_id={}&scope=photos,audio,video,docs,notes,pages,status,offers,questions,wall,groups,email,notifications,stats,ads,offline,docs,pages,stats,notifications&response_type=token"

    def __init__(self):
        for i in range(len(proxies)):
            proxy = f"{proxies[i]['type']}://{proxies[i]['ip']}:{proxies[i]['port']}"

            for bot in bots[i*len(proxies):(i*len(proxies)) + len(proxies)]:
                bot_raw = bot.replace("\n", "").split(":")
                bot_path = Path().joinpath("Данные для работы", "Социалочка", "Аккаунты", "ВК", f"{bot_raw[0]}.json")

                if not bot_path.exists():
                    # has_app = int(input(f"Бот: {bot_raw[0]} -> не найден Access Token. У вас есть зарегестрированное Standalone приложение?\n1 - Да, 0 - Нет"))
                    print(f"""
Необходимо создать Standalone приложение. 
1) https://vk.com/ - Зайдите в профиль {bot_raw[0]} (Пароль: {bot_raw[1]})
2) https://vk.com/apps?act=manage - Перейдите по ссылке
3) Выберите/Создайте Ваше приложение и скопируйте ID
                    """)
                    app_id = int(input("Введите ID Вашего приложения\n"))

                    print(f"""
https://oauth.vk.com/authorize?client_id={app_id}&scope=photos,audio,video,docs,notes,pages,status,offers,questions,wall,groups,email,notifications,stats,ads,offline,docs,pages,stats,notifications&response_type=token
Перейдите по ссылке, дайте приложению необходимые разрешения и скопируйте адресную строку
                    """)

                    bot_token = str(input("Вставьте скопированную адресную строку\n")).split("access_token=")[1].split("&")[0]
                    print(f"Ваш токен: {bot_token}")

                    number_changed = int(input(f"Вам потребовалось изменять номер телефона при регистрации приложения?\n0 - Нет, 1 - Да\n"))
                    if number_changed == 1:
                        number = self.check_number(
                            int(input(f"Введите новый номер телефона для доступа к ВКонтакте. Предыдущий номер: {bot_raw[0]}\n")))
                    else:
                        number = bot_raw[0]

                    with open(bot_path, "w+", encoding="utf-8") as f:
                        dump({
                            "login": number,
                            "password": bot_raw[1],
                            "user_id": bot_raw[2],
                            "app_id": app_id,
                            "access_token": bot_token
                        }, f)
                
                # with open(bot_path, "r+", encoding="utf-8") as f:
                #     bot_data = load(f)
                # # print(bot_data)
                # # sleep(randint(50, 70))
                # if self.auth(bot_data, proxy) == True:
                #     for group in self.bot_session.method("groups.get", {
                #         "user_id": my_user_id,
                #         "extended": 1
                #     })["items"]:
                #         if self.our_posts_likes(group, bot_data["login"]) == 17:
                #             break

    def auth(self, bot, proxy):
        try:
            self.session.proxies = {
                "http": proxy
            }

            self.bot_session = vk_api.VkApi(bot["login"], bot["password"], bot["access_token"], auth_handler, session=self.session)
            self.bot_session.auth()

            self.respond_text = f"Бот: {bot['login']}, авторизация успешна. Начинаю выполнение скрипта..."

            return True
        except Exception as e:
            self.respond_text = f"Аккаунт: {bot['login']} -> не удалось авторизоваться. (Ошибка: {e})"

            return False

        print(self.respond_text)
        alarm(os.path.basename(__file__), self.respond_text)


    def check_number(self, number):
        while not bool(match(r'[78]?\d{10}$', str(number))):
            number = int(input(f"Ошибка! Вы ввели номер телефона в неверном формате. Повторите попытку ввода\n"))
        else:
            return number

    def our_posts_likes(self, group, user):
        for post in self.bot_session.method("wall.get", {
            "owner_id": -group["id"],
            "count": 40,
            "extended": 1
        })["items"]:
            # print(group["name"], post["views"]["count"] or post["text"])
            if randint(1, 99) % 5 == 0 and (post["from_id"] == my_user_id or (
                "signed_id" in post and (post["signed_id"] == my_user_id)
            )):
                sleep(randint(10, 20))
                if self.bot_session.method("likes.isLiked", {
                    "type": "post",
                    "item_id": post["id"]
                })["liked"] == 0:
                    try:
                        self.bot_session.method("likes.add", {
                            "type": "post",
                            "item_id": post["id"],
                            "owner_id": post["owner_id"]
                        })

                        self.respond_text = f"Бот: {user}, поставили лайк нашей публикации в группе {group['name']}"
                    except vk_api.ApiError as e:
                        if e.code != 17:
                            self.respond_text = f"Бот: {user} (Ошибка: {e})"
                        else:
                            return e.code
                else:
                    self.respond_text = f"Бот: {user} -> Уже ставили лайки в группе {group['name']}"

                print(self.respond_text)
                alarm(os.path.basename(__file__), self.respond_text)


    def if_member(self, group, user):
        try:
            if self.bot_session.method("groups.isMember", {
                "group_id": group["id"],
            }) == 0:
                self.bot_session.method("groups.join", {
                    "group_id": group["id"]
                })
                
                self.respond_text = f"Бот: {user} -> Подписались на группу {group['name']}"
        except vk_api.ApiError as e:
            if e.code != 17:
                self.respond_text = f"Бот: {user} -> Ошибка! ({e})"
            else:
                return e.code
        
        print(self.respond_text)
        alarm(os.path.basename(__file__), self.respond_text)

    # def get_bots(self):
    #     print(self.bots)

                # print(get(url="http://google.com/", proxies=f'{self.proxies[i]["ip"]}:{self.proxies[i]["port"]}', auth=auth.HTTPProxyAuth(self.proxies[i]["username"], self.proxies[i]["password"])))

class Activity():
    exit = False
    respond_text = ""
    scopes = "OFFLINE"
    counter = 0
    members_edge = 700
    groups_pass_counter = 0
    how_many_pass = 40
    path = os.path.join(
        "Данные для работы",
        "Социалочка",
        "Посты",
        "ВК"
    )
    def __init__(self):
        with open(Path(self.path).joinpath("1.json"), "r+", encoding="utf-8") as f:
            self.bd = load(f)

        self.session = vk_api.VkApi(
            my_user, my_password, my_app_token, auth_handler)
        self.session.auth()

        self.fast_method = self.session.get_api()
        self.upload = vk_api.VkUpload(self.session)

        self.my_id = self.fast_method.users.get()[0]["id"]
        self.our_group = -self.session.method("groups.getById", {
            "group_ids": "familyanrossosh"
        })[0]["id"]
        self.how_many_groups = self.session.method("groups.get")["count"]

    def posts(self):
        for group in self.session.method("groups.get", {
            "extended": 1
        })["items"]:
            if self.exit != True:
                if -group["id"] != self.our_group:
                    try:
                        if (self.check_group_len(group) and self.check_wall_posts(group)) != False:
                            for obj in self.bd["objs"]:
                                memes = [f"photo{photo['owner_id']}_{photo['id']}" for photo in self.upload.photo_wall(
                                    self.bd["memes"][ : 2], None, None, None)]
                                try:
                                    attachments = [f"photo{photo['owner_id']}_{photo['id']}" for photo in self.upload.photo_wall(
                                        self.bd["objs"][obj]["photos"], None, None, self.bd["objs"][obj]["text"])]
                                except:
                                    attachments = []

                                if "youtube" in self.bd["objs"][obj]:
                                    attachments.append(self.bd["objs"][obj]["youtube"])
                                else:
                                    attachments.append(self.bd["objs"][obj]["vk"])

                                self.session.method("wall.post", {
                                    "owner_id": -group["id"],
                                    "from_group": 0,
                                    "message": f"{self.bd['objs'][obj]['text']}\n{self.bd['objs'][obj]['avito']}",
                                    "attachments": ",".join(attachments)
                                })
                                self.respond_text = f"Сделали посты в группу {group['name']}! (Посты: {'; '.join(self.bd['objs'])}"
                                # print(self.respond_text)
                                # alarm(os.path.basename(__file__), self.respond_text)
                        else:
                            self.respond_text = f"Уже делали посты в группу {group['name']}"
                        
                        self.how_many_groups -= 1
                            # print(self.respond_text)
                            # alarm(os.path.basename(__file__), self.respond_text)
                            # break
                    except vk_api.ApiError as e:
                        if e.code != 220:
                            if group["is_admin"] != 1 and (e.code != 15):
                                self.respond_text = f"Отписались от группы {group['name']} (Ошибка: {e})"

                                self.session.method("groups.leave", {
                                    "group_id": group["id"] 
                                })
                        else:
                            self.respond_text = "Слишком увлеклись! Прерываю работу скрипта."
                            self.exit = True
                            # print()
                    except Exception as e:
                        self.respond_text = f"Ошибка: {e}"

                    print(f"{self.respond_text}\nОсталось групп: {self.how_many_groups}")
                    alarm(os.path.basename(__file__), f"{self.respond_text}\nОсталось групп: {self.how_many_groups}")
                else:
                    break
    
    def our_group_posts(self):
        # print(self.bd["news"])
        # exit()
        for news in self.bd["news"]:
            sleep(randint(100, 350))
            # if False not in self.check_wall_posts(self.our_group, news):
            self.session.method("wall.post", {
                "owner_id": self.our_group,
                "from_group": 1,
                "message": news.split("Ссылка на новость: ")[0],
                "attachments": news.split("Ссылка на новость: ")[1]
            })
            self.respond_text = f"Отправили новость в нашу группу:\n{news.split('Ссылка на новость: ')[0]}"

            print(self.respond_text)
            alarm(os.path.basename(__file__), self.respond_text)

        # for mem in memes:
        #     self.session.method("wall.post", {
        #         "owner_id": -group["id"],
        #         "from_group": 1,
        #         "attachments": mem
        #     })
        # print(f"Отправили мемы в нашу группу!)")

    def check_group_len(self, group):
        if(self.session.method("groups.getMembers", {
            "group_id": group["id"]
        })["count"] <= self.members_edge) and (group["is_admin"] != 1):
            self.respond_text = f"Отписались от группы {group['name']} (Количество подписчиков менее {self.members_edge})"
            
            self.session.method("groups.leave", {
                "group_id": group["id"]
            })
            # print(self.respond_text)
            # alarm(os.path.basename(__file__), self.respond_text)

            return False
        else:
            return True

    def check_wall_posts(self, group, text_to_check=None):
        result = []

        # try:
        for post in self.session.method("wall.get", {
            "owner_id": -group["id"],
            "count": 120,
            "extended": 1
        })["items"]:
            if (post["from_id"] != self.my_id) and (
                group["is_admin"] == 1) or (
                    post["from_id"] == self.my_id) or (
                        "signed_id" in post and (post["signed_id"] == self.my_id)):
                        # if post["text"] != text_to_check:
                        #     result.append(True)
                        # else:
                        #     result.append(False)
                        
                        if post["likes"]["count"] <= len(bots) and (
                                post["comments"]["count"] == 0):
                                print(post["comments"]["count"])
                                # exit()
                                try:
                                    self.session.method("wall.delete", {
                                        "owner_id": post["owner_id"],
                                        "post_id": post["id"]
                                    })
                                    result.append(True)

                                    print(
                                        f"Удалили устаревший пост из группы {group['name']}")
                                except Exception as e:
                                    result.append(False)

                                    print(
                                        f"Не удалось удалить наш пост из группы {group['name']} ({e})")


        
        return result
if len(argv) > 2:
    print(f"Скрипт: {argv[1]} -> {argv[2]}")
    alarm(os.path.basename(__file__), f"{argv[1]} -> {argv[2]}")
    
    exec(f"{argv[1]}().{argv[2]}()")
elif len(argv) == 2:
    print(f"Скрипт: {argv[1]}")
    alarm(os.path.basename(__file__), f"{argv[1]}")
    try:
        exec(f"{argv[1]}()")
    except:
        exec(f"{argv[1]}('{argv[2]}')")
# else:
