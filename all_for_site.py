from ftplib import FTP
from PIL import Image
import os, glob, json, shutil, pathlib

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
home_dir = os.path.join(
    'C:\\',
    'Users',
    'proka',
    'virtuals',
    'python',
    'django',
    'rossoshrealty',
    'familyan'
    )
list_of_dirs = [
    os.path.join(home_dir, 'media', 'images', 'raw', 'properties'),
    os.path.join(home_dir, 'media', 'images', 'we'),
    os.path.join(home_dir, 'media', 'rss'),
    os.path.join(home_dir, 'media', 'bd'),
    os.path.join(home_dir, 'media', 'texts'),
]

class Basic():
# Функция проверки последнего изменения файла каталога
    # def check_change_in_catalog(path):
    #     # hist_date = 
    #     catalog_date = os.path.getmtime(path):
        
# Создаём внутри корневого каталога сайта рабочие папки
    def check_dirs(self, paths):
        for path in paths:
            if not os.path.exists(path):
                os.mkdir(path)
            # else:
            #     print('{0} - OK'.format(path))
            else:
                shutil.rmtree(path)
                os.mkdir(path)
#Совокупность функций для работы с информацией для сайта
class Info():
    with open(
        os.path.join(
            'Данные для работы',
            'Социалочка',
            'Каталог.json'
            ), encoding = 'utf-8'
        ) as f:
            objs = json.load(f)
    
    team = [
        'Agent',
        'Law'
    ]

    dist_rss = os.path.abspath(
            search(
                os.path.join(
                    home_dir,
                    'media',
                    'rss'
                    )
                )
            )
    dist_texts = os.path.abspath(
                search(
                    os.path.join(
                        home_dir,
                        'media',
                        'texts'
                        )
                    )
                )
    dist_bd = os.path.abspath(
            search(
                os.path.join(
                    home_dir,
                    'media',
                    'bd'
                    )
                )
            )
    dist_photo_member = os.path.abspath(
                search(
                    os.path.join(
                        home_dir,
                        'media',
                        'images',
                        'we'
                        )
                    )
                )

    def rss(self):
        rss_path = search(
            os.path.join(
                'Данные для работы',
                'Социалочка',
                'Список RSS каналов.txt'
                )
            )

        shutil.copy(rss_path, self.dist_rss)
        os.rename(
                os.path.join(self.dist_rss, 'Список RSS каналов.txt'),
                os.path.join(self.dist_rss, 'rss_list.txt')
            )
    def text(self):
        for obj in sorted(self.objs):
            text_path = search(
                os.path.join(
                    'Данные для работы',
                    'Авито',
                    f'{self.objs[obj]["Адрес"]}.txt'
                    )
                )

            shutil.copy(text_path, self.dist_texts)
            os.rename(
                search(os.path.join(self.dist_texts,f'{self.objs[obj]["Адрес"]}.txt')),
                os.path.join(self.dist_texts, f'{self.objs[obj]["id"]}.txt')
            )
# Функция копирования файлов БД в каталог dist_path_bd
    def bd(self):
        catalog = {
            'origin': os.path.join('Данные для работы', 'Социалочка', 'Каталог.json'),
            'name': 'Каталог.json',
            'rename': 'catalog.json',
        }
        bd_we = {
            'origin': search(os.path.join('Данные для работы', 'Социалочка', 'Наши ресурсы.json')),
            'name': 'Наши ресурсы.json',
            'rename': 'we.json',
        }
        services = {
            'origin': search(os.path.join('Данные для работы', 'Социалочка', 'Наши услуги.json')),
            'name': 'Наши услуги.json',
            'rename': 'services.json',
        }
        for bd in catalog, bd_we, services:
            shutil.copy(bd['origin'], self.dist_bd)
            os.rename(
                search(os.path.join(self.dist_bd, bd['name'])),
                os.path.join(self.dist_bd, bd['rename'])
            )

        for obj in sorted(self.objs):
            bd_path = search(
                os.path.join(
                    'Данные для работы',
                    'БД',
                    f'{self.objs[obj]["Адрес"]}.json'
                    )
                )

            # if not os.path.exists(dist_path_bd):
            shutil.copy(bd_path, self.dist_bd)
            os.rename(
                search(os.path.join(self.dist_bd, f'{self.objs[obj]["Адрес"]}.json')),
                os.path.join(self.dist_bd, f'{self.objs[obj]["id"]}.json')
                )
# Функция копирования Фото в каталог dist_path_photo
    def photo(self):
        for member in self.team:
            member_face_path = search(
                os.path.join(
                    'Данные для работы',
                    'Фотобанк',
                    'Сотрудники',
                    '{}.jpeg'.format(member)
                    )
                )

            # if not os.path.exists(dist_member_path):
            shutil.copy(member_face_path, self.dist_photo_member)

        for obj in sorted(self.objs):
            Basic().check_dirs([
                os.path.join(
                    home_dir,
                    'media',
                    'images',
                    'raw',
                    'properties',
                    f'{self.objs[obj]["id"]}'
                    )
                ])

            photo_path = search(
                os.path.join(
                    'Данные для работы',
                    'Фотобанк',
                    self.objs[obj]['Адрес']
                    )
                )
            photo_face_path = search(
                os.path.join(
                    'Соц.Сети',
                    self.objs[obj]['Адрес'],
                    'Морда.jpeg'
                    )
                )
            dist_path_photo = os.path.abspath(
                search(
                    os.path.join(
                        home_dir,
                        'media',
                        'images',
                        'raw',
                        'properties',
                        f'{self.objs[obj]["id"]}'
                        )
                    )
                )

            # if not os.path.exists(photo_face_path):
            shutil.copy(photo_face_path, dist_path_photo)
            os.rename(
                os.path.join(dist_path_photo, 'Морда.jpeg'), 
                os.path.join(dist_path_photo, 'face.jpeg')
            )

            for dirs in pathlib.Path(photo_path).iterdir():
                if dirs.is_dir():
                    files = [file for file in pathlib.Path(dirs).iterdir() if file.stat().st_size > 0 and file.exists()]

                    if 'Нефильтрованное' not in dirs.name:
                        for photo in files[0 : len(files) // 2 + 1 : 2]:
                            # print(photo)
                            shutil.copy(photo, dist_path_photo)
                    # else:
                    #     for photo in files:
                    #         # print(photo)
                    #         shutil.copy(photo, dist_path_photo)

    def ftp(self):
        base = pathlib.Path(home_dir).iterdir()

        ftp_host = 'vh308.timeweb.ru'
        ftp_user = 'ca45106'
        ftp_password = 'Tz2k44Z6h6Yo'

        # ftp = FTP(ftp_host, ftp_user, ftp_password)
        # ftp.cwd('rossoshrealty')
        # print(ftp.getwelcome())

        for dir in base:
            if dir.is_dir():
                for smth in pathlib.Path(dir).iterdir():
                    if smth.is_dir():
                        for smth_2 in pathlib.Path(smth).iterdir():
                            print(smth_2)
                            if smth_2.is_dir():
                                for smth_3 in pathlib.Path(smth_2).iterdir():
                                    print(smth_3)
                                    if smth_3.is_dir():
                                        for smth_4 in pathlib.Path(smth_3).iterdir():
                                            print()
                    else:
                        print(smth)



# Basic().check_dirs(list_of_dirs)
# Info().text()
# Info().rss()
# Info().bd()
# Info().photo()
Info().ftp()