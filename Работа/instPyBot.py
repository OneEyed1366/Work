import os
import shutil
from Alarmer import alarm
from instagrapi import Client
from instapy import InstaPy, smart_run
from json import load, dump
from pathlib import Path
from sys import argv, exit
from myigbot import MyIGBot
from instabot import Bot
from time import sleep
from datetime import date, datetime
from random import randrange, randint

logs = []
limits_path = Path().joinpath("Данные для работы","Социалочка", "Лимиты", "Inst.json")
logs_file_path = Path().joinpath(
    "Данные для работы", "Боты","События",
    os.path.basename(__file__),
    f"{date.today()}.txt"
    )
my_users = {
    "work": {
        "login": "familyan.rossosh",
        "password": "fcg345"
    },
    "personal": {
        "login": "psevdoproger",
        "password": "Ka8iDz.Oo"
    }
}

if len(argv) > 1:
    my_user = my_users[argv[1]]["login"]
    my_password = my_users[argv[1]]["password"]
    acc = argv[1]
else:
    my_user = my_users["work"]["login"]
    my_password = my_users["work"]["password"]
    acc = "work"

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

with open(
    limits_path,
    "a+", encoding="utf-8"
) as f:
    try:
        limits = load(f)
    except:
        limits = {
            "work": {
                "following": 3,
                "likes": 5,
                "succesful": 0,
                "succesful_days": 0,
                "allow_to_experiment": True
            },
            "personal": {
                "following": 3,
                "likes": 5,
                "succesful": 0,
                "succesful_days": 0,
                "allow_to_experiment": True
            }
        }

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

complete = 0
errs = 0

# bot = MyIGBot(my_user, my_password)
# py_bot = InstaPy(username=my_user, password=my_password).login()
# bot = Client()
# bot.login(my_user, my_password)
bot = Bot()
bot.login(username=my_user, password=my_password)
# print(
#     f"""Количество успешных выполнений скрипта: {limits[acc]['succesful_days']}
# Можно ли эксперементировать: {limits[acc]['allow_to_experiment']}
# Лимиты на сегодня:
# Лайки: {limits[acc]['likes']}
# Подписки: {limits[acc]['following']}"""
#     )

alarm(f"{os.path.basename(__file__)}\nАккаунт: {acc}")

# Работает:
#   1.Получение подписчиков/подписок из личного аккаунта
#   2.Получение {how_many} последних постов у каждого полученного аккаунта
#     .1.Получение комментариев к каждому посту
#     .2.Получение пользователей, оставивших комментарии
#       .1.Получение подписчиков/подписок пользователей, оставивиших комментарии
#   3.Проставление лайков постам пользователей
#   4.Подписка/Отписка на пользователей
#       .1.Запись в файл имени пользователя и даты подписки
#       .2.Проверка даты подписки на пользователя, если больше 3 дней - отписка и работа со следующим пользователем
#   5.Постинг в Фото/Видео в Ленту/Истории
#     .1.Проданные объекты с необходимой информацией
#     .2.Мемы
#   6.Комментирование постов пользователей
# Что нужно сделать:
#   1.Автоматический постинг из уже готовых файлов
#     .1.Объекты
#       1.Новый объект (Видео)
#     .2.Истории
#   2.Глобально - работа в наиболее активные часы
#       .1.Постинг
#           .1.Посты в наиболее активные часы
#       .2.Подписичики

# class Cleaning():
#     count = 0
#     # print(followers)
#     exit()
#     def __init__(self):
#         try:
#             for follower in self.my_followers[ : self.how_many]:
#                 relax = randrange(20, 50)

#                 print(f"Отдыхаем!.. (Секунд: {relax})")
#                 sleep(relax)

#                 if my_user not in bot.get_user_followers(follower):
#                     bot.unfollow(follower)
#                     print(f"Отписались от пользователя {follower}")

#                     self.count += 1
#                     logs.append(f"Отписались от пользователя {follower}")
#                 else:
#                     print(f"Есть взаимная подписка на пользователя {follower}")

#                     logs.append(
#                         f"Есть взаимная подписка на пользователя {follower}")
#             print(f"Удалено невзаимных подписчиков: {self.count}")

#             logs.append(f"Удалено невзаимных подписчиков: {self.count}")
#         except KeyboardInterrupt:
#             print("Прерываю очистку профиля по инициативе пользователя!")

#             logs.append("Прерываю очистку профиля по инициативе пользователя!")
#         except:
#             print("Упс! не получилось почистить профиль от мусора!")

#             logs.append("Упс! не получилось почистить профиль от мусора!")
        

# Постинг
class Posting():
    respond_text = ""
    path = os.path.join(
        "Данные для работы",
        "Социалочка",
        "Посты",
        "Inst"
    )
    new = [i for i in Path(path).iterdir() if Path(i).is_dir()]
    memes = [i for i in Path(path).glob("*.jpeg")]
    used = [i for i in Path(path).glob("*.REMOVE_ME")]
    selled = [i for i in Path(path).joinpath("Продано").glob("*.json")]
    # print(len(selled))
    def __init__(self, how_many):
        self.count = 0
# # Если есть новые объекты - добавляем их
#                 if len(self.new) > 0:
#                     print(f"Количество новых объектов: {len(self.new)}. Начинаю постинг...")

#                     for obj in self.new:
#                         b
# Удаляем уже использованные мемы
        for file in self.used:
            os.remove(file)
# Делаем посты мемов на стену
        # self.respond_text = f"Кол-во файлов для публикации: {how_many}"

        for mem in self.memes[ : how_many + 1]:
            sleep(randrange(3, 15))
            if bot.upload_photo(
                    mem,
                    "#россошь #россошь36 #мемы #риэлтор"
                ):
                self.count += 1
                self.respond_text = f"{self.count} мем пошел!)"
            else:
                self.respond_text = f"Ошибка! Не смогла найти файл {os.path.basename(mem)}"
                os.remove(mem)

            print(self.respond_text)
            alarm(os.path.basename(__file__), self.respond_text)
# Если есть какие-либо проданные объекты - делаем посты на стену
        # print(self.selled)
        if len(self.selled) > 0:
            for obj in self.selled:
                sleep(randrange(3, 15))
                try:
                    with open(obj, encoding="utf-8") as db:
                        dict = load(db)

                        bot.upload_photo(
                            search(os.path.abspath(os.path.join(
                                os.path.join(self.path, "Продано"),
                                dict["Фото"]))),
                            dict["Текст"]
                        )

                        self.respond_text = "Сделали пост о продаже объекта"
                except:
                    self.respond_text = f"Хм, не могу получить доступ к файлу..."
            
            shutil.rmtree(os.path.join(self.path, "Продано"))
            os.mkdir(os.path.join(self.path, "Продано"))
        else:
            self.respond_text = "Нет неопубликованных проданных объектов!"
            
        print(self.respond_text)
        alarm(os.path.basename(__file__), self.respond_text)

class Followers():
    respond_text = ""
    my_followings = bot.get_user_following(my_user)

    def __init__(self, how_many):
        try:
            for following in self.my_followings[ : how_many + randrange(5, 10)]:
                for post in bot.get_user_medias(following, is_comment=True):
                    for commenter in bot.get_media_commenters(post):
                        if commenter not in self.my_followings:
                            bot.follow(commenter)

                            self.my_followings.append(commenter)
        except KeyboardInterrupt:
            self.respond_text = "Прерываю команду по инициативе пользователя"
        
        print(self.respond_text)
        alarm(os.path.basename(__file__), self.respond_text)

# Продвижение
class Liking():
    respond_text = ""
    following = 0
    likes = 0
    followers_errors = errs
    path = os.path.join(
        "Данные для работы",
        "Социалочка",
        "Посты",
        "Inst"
    )
    list_of_hashtags = {
        "work": [
            "россошь36",
            "россошь136",
            "россошь",
            "риэлтор",
            "россошьфото",
            "россошьотдых",
            "россошьподарки",
            "россошьцветы",
            "россошьмастеркласс",
            "россошькафе",
            "россошьновости"
        ],
        "personal": [
            "python",
            "dev",
            "js",
            "javascript",
            "proger",
            "programming",
            "sport",
            "fitness",
            "classicalmusic",
            "jrock",
            "rock",
            "kpop"
        ]
    }
    accs = bot.get_user_following(my_user)

    def __init__(self, how_many):
        if randrange(1, 10) % 2 == 0:
            self.respond_text = "Работаем с подписчиками!"

            print(self.respond_text)
            alarm(os.path.basename(__file__), self.respond_text)
            bot.unfollow_non_followers(how_many + randrange(1, 3))
            bot.like_following(my_user, how_many + randrange(1, 3))
            bot.like_followers(my_user, how_many + randrange(1, 3))
            # self.posts = [bot.get_user_medias(i) for i in bot.get_user_following(my_user) if len(bot.get_user_medias(i)) != 0]
        else:
            self.respond_text = "Работаем с хештегами!"

            print(self.respond_text)
            alarm(os.path.basename(__file__), self.respond_text)

            for hashtag in self.list_of_hashtags[acc]:
                bot.like_hashtag(hashtag, how_many + randrange(1, 4))

            # self.posts = [bot.get_hashtag_medias(i, filtration=False)[:5] for i in self.list_of_hashtags[acc] if len(bot.get_hashtag_medias(i)) != 0]
        
        # for post_groups in self.posts:
        #     relax = randrange(20, 50)

        #     print(f"Отдыхаем!.. (Секунд: {relax})")
        #     sleep(relax)
        #     for post in post_groups:
        #         # print(bot.get_media_info(post[0]["pk"]))
        #         try:
        #             user_id = bot.get_media_owner(post)
        #             username = bot.get_username_from_id(user_id)

        #             # if (not bot.follow(user)) and (
        #             #     my_user not in bot.get_user_following(user)
        #             # ):
        #             #     sleep(randrange(3, 15))
        #             #     bot.unfollow(user)
        #             #     self.accs.append(user)

        #             #     print(f"Отписались от пользователя: {user}")

        #             #     logs.append(f"Отписались от пользователя: {user}")
        #             # else:
        #                 # print(bot.get_user_stories(user))
        #             # for story in bot.get_user_stories(user_id):
        #             #     sleep(randrange(3, 15))
        #             #     if bot.watch_users_reels(bot.get_media_id_from_link(story)):
        #             #         print(
        #             #             f"Посмотрели историю пользователя {username}")

        #             # exit()
        #             sleep(randrange(3, 15))
        #             # if self.likes <= limits[acc]["likes"]:
        #             if bot.like(post[0]["pk"]):
        #                 print(
        #                     f"Поставили лайк публикации пользователя {username}")

        #                 logs.append(
        #                     f"Поставили лайк публикации пользователя {username}")
                        
        #                 # if (limits[acc]["allow_to_experiment"] == True) and (
        #                 #     limits[acc]["succesful"] == 1):
        #                 #     limits[acc]["likes"] += 1

        #                 # self.likes += 1
        #             else:
        #                 print("Ошибка с лайками! Пробую продолжить, а там как пойдет...")

        #                     # limits[acc]["likes"] -= 3

        #             sleep(randrange(3, 15))
        #             if username != my_user and (
        #                 user_id not in self.accs):
        #                 if bot.follow(username):
        #                     print(
        #                         f"Пользователь: {username}, подписка активна")
        #                     logs.append(
        #                         f"Пользователь: {username}, подписка активна")

        #                     # if (limits[acc]["allow_to_experiment"] == True) and (
        #                     #     limits[acc]["succesful"] == 1):
        #                     #     limits[acc]["following"] += 1

        #                     self.accs.append(user_id)
        #                     # self.following += 1
        #                 else:
        #                     print("Ошибка с подпиской! Пробую продолжить, а там как пойдет...")

        #                     # limits[acc]["following"] -= 2

        #         except KeyboardInterrupt:
        #             print("Прерываю команду по инициативе пользователя!)")
        #             logs.append(f"Прерываю команду по инициативе пользователя!)")

        #             exit()

                # except:
                #     print(f"Ошибка! Пробую продолжить, а там как пойдет...")
                #     f.write(
                #         f"\nОшибка! Пробую продолжить, а там как пойдет...")

                #     self.followers_errors += 1

class Behavior():
    def __init__(self):
        self.scripts = [
            "Posting",
            "Liking",
            "Followers"
        ]
        for script in [f"{self.scripts[randint(0, 1)]}" for i in range(3)]:
            try:
                eval(script + f"({randrange(1, 3)})")
            except:
                eval(f"{script}()")

#   Общая идея:
#       Каждый скрипт запускается в случайно сгенерированном порядке
#   Что нужно сделать:
#       1. Поддержание работоспособности скрипта до определенного промежутка времени
#   Сделано:
#       1. Генерацию случайной последовательности выполнения скриптов
#           .1. Записывать последовательность скриптов в переменную
#               .1. Генерировать для каждого скрипта собственные входные данные
#       2. Запуск скриптов в соотвествии с последовательностью

if errs < 2:
    try:
        if len(argv) > 2:
            print(f"Скрипт: {argv[2]}, аккаунт: {argv[1]}")
            try:
                eval(f"{argv[2]}()")
            except:
                eval(f"{argv[2]}({randrange(1, 3)})")

        elif len(argv) == 2:
            print(f"Стандартный сценарий, аккаунт: {argv[1]}")

            Behavior()
        else:
            Behavior()

        print("instPyBot - выполнение завершено!")
        alarm("instPyBot - выполнение завершено!")
    except KeyboardInterrupt:
        print("Прерываю команду по инициативе пользовтеля!)")
        alarm("Прерываю команду по инициативе пользовтеля!)")
    except:
        print(f"Ошибка! Пробую продолжить, а там как пойдет...")
        alarm("Ошибка! Пробую продолжить, а там как пойдет...")

        errs += 1
else:
    print("Ой-ей, слишком много ошибок! :( Завершаю работу скрипта!")
    alarm("Ой-ей, слишком много ошибок! :( Завершаю работу скрипта!")

with open(logs_file_path, "a+", encoding="utf-8") as f:
    for log in logs:
        f.write(f"\n{log}")

with open(limits_path, "w+", encoding="utf-8") as f:
    if errs == 0:
        limits[acc]["succesful"] == 1
        limits[acc]["succesful_days"] += 1
    else:
        limits[acc]["succesful"] == 0
        limits[acc]["succesful_days"] == 0

    if limits[acc]["succesful_days"] == 5:
        limits[acc]["allow_to_experiment"] == False
    else:
        limits[acc]["allow_to_experiment"] == True

    dump(limits, f)
