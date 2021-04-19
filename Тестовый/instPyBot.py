from instagrapi import Client
import pathlib
import os
import json
import shutil
from time import sleep

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

cl = Client()
cl.login("familyprokson", "255irinaPro")

class Posting():
  path = os.path.join(
      "Данные для работы",
      "Социалочка",
      "Посты",
      "Inst"
  )

  def wall_mem(self, how_many = 1):
      extensions = [
          "*.jpeg",
          "*.png",
          "*.tiff"
      ]

      for ext in extensions:
        for mem in pathlib.Path(self.path).glob(ext):
            cl.photo_upload(
                mem,
                "#россошь #россошь36 #мемы #риэлтор"
            )

            os.remove(mem)
          
          # break

  def wall_selled(self):
      if pathlib.Path(os.path.join(self.path, "Продано")).stat().st_size > 0:
          for obj in pathlib.Path(os.path.join(self.path, "Продано")).glob("*.json"):
              with open(obj, encoding="utf-8") as f:
                  dict = json.load(f)

                  cl.photo_upload(
                      os.path.abspath(os.path.join(
                          os.path.join(self.path, "Продано"),
                          dict["Фото"])),
                      dict["Текст"]
                  )

          shutil.rmtree(os.path.join(self.path, "Продано"))
          os.mkdir(os.path.join(self.path, "Продано"))

  def stories_objs(self, obj):
      for photo in obj:
          cl.photo_upload_to_story(obj)

class Followers():
  path = os.path.join(
      "Данные для работы",
      "Социалочка",
      "Посты",
      "Inst"
  )

  my_id = cl.user_id_from_username("familyprokson")
  my_followers = cl.user_followers(my_id, amount = 1)

  def check_profiles(self):
      watched_path = os.path.join(self.path, "Использованные.txt")

      if os.path.exists(watched_path):
          with open(watched_path, "r+") as f:
              watched = f.read()
      else:
          with open(watched_path, "w+") as f:
              watched = f.read()

      if sum(1 for i in watched) == sum(1 for i in self.my_followers):
          with open(watched_path, "w+") as f:
              watched = f.read()

      return {
          "watched": watched,
          "watched_path": watched_path
      }
  def like__posts_and_follow_users_by_hashtags(self, how_many=5):
    for hashtag in cl.hashtag_related_hashtags("россошь36"):
      print(hashtag)
      for post in cl.hashtag_medias_recent(hashtag, how_many):
          cl.media_like(post.id)

          if cl.media_user(post) not in self.my_followers:
              cl.user_follow(cl.media_user(post))
              print(
                  f"Пользователь: {cl.username_from_user_id(cl.media_user(post))}, подписка активна"
              )
          else:
            print(post, hashtag)

  def like_posts_and_watch_stories(self, how_many = 5):
      watched = self.check_profiles()["watched"]

      with open(self.check_profiles()["watched_path"], "a+") as f:
          for follower in self.my_followers:
              if cl.username_from_user_id(follower) not in watched:
                  for follower_post in cl.user_medias(follower, how_many):
                      cl.media_like(follower_post.id)
                      # cl.media_like(follower_post)

                  print(
                      f"Пользователь: {cl.username_from_user_id(follower)}, количество лайков: {how_many}")
                  f.write(f"\n{cl.username_from_user_id(follower)}")
              else:
                  # print(
                      # f"Уже посещали профиль {cl.username_from_user_id(follower)}"
                  # )
                  pass

#   Что нужно сделать:
#       1.Отписка от тех, кто не подписался на меня в ответ
  def follow_followers_commentators(self, how_many = 3):
      
      for follower in self.my_followers[ : 1]:
          for follower_post in cl.user_medias(follower, how_many):
              for comment in cl.media_comments(follower_post.id)[: 1]:
                  i = 0

                  for commenter_follower in cl.user_followers(cl.user_id_from_username(comment.user.username)):
                      if (i != how_many) and (commenter_follower not in self.my_followers):
                          cl.user_follow(commenter_follower)
                          print(
                              f"Пользователь: {cl.username_from_user_id(commenter_follower)}, подписка: активна")

                          i += 1
                      else:
                          # print(
                          #     f"Пользователь: {cl.username_from_user_id(commenter_follower)} уже среди наших подписчиков")

                          break

# Posting().wall_mem(2)
Followers().like__posts_and_follow_users_by_hashtags(3)