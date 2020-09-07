from ftplib import FTP
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
        
        
with open(
    os.path.join(
        'Данные для работы',
        'Социалочка',
        'Каталог.json'
        ), encoding = 'utf-8'
    ) as f:
        objs = json.load(f)

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
    os.path.join(home_dir, 'static', 'images', 'Объекты'),
    os.path.join(home_dir, 'static', 'images', 'Команда'),
    os.path.join(home_dir, 'static', 'bd'),
]
team = [
    'Агент',
    'Юрист'
]
class Basic():
# Функция проверки последнего изменения файла каталога
    def check_change_in_catalog(path):
        # hist_date = 
        catalog_date = os.path.getmtime(path):
        
# Создаём внутри корневого каталога сайта рабочие папки
    def check_dirs(paths):
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
# Функция копирования файлов БД в каталог dist_path_bd
    def copy_bd(objects):
        for obj in objects:
            dist_path_bd = os.path.abspath(
                search(
                    os.path.join(
                        home_dir,
                        'static',
                        'bd'
                        )
                    )
                )
            bd_path = search(
                os.path.join(
                    'Данные для работы',
                    'БД',
                    '{}.json'.format(objs[obj]['Адрес'])
                    )
                )

            if not os.path.exists(dist_path_bd):
                shutil.copy(bd_path, dist_path_bd)
# Функция копирования Фото в каталог dist_path_photo
    def copy_photo(objects, team):
        for member in team:
            member_face_path = search(
                os.path.join(
                    'Данные для работы',
                    'Фотобанк',
                    'Сотрудники',
                    '{}.jpeg'.format(member)
                    )
                )

            dist_member_path = os.path.abspath(
                search(
                    os.path.join(
                        home_dir,
                        'static',
                        'images',
                        'Команда'
                        )
                    )
                )
            if not os.path.exists(dist_member_path):
                shutil.copy(member_face_path, dist_member_path)

        for obj in objects:
            Basic.check_dirs([
                os.path.join(
                    home_dir,
                    'static',
                    'images',
                    'Объекты',
                    '{}'.format(objs[obj]['Адрес'])
                    )
                ])

            photo_path = search(
                os.path.join(
                    'Данные для работы',
                    'Фотобанк',
                    '{}'.format(objs[obj]['Адрес'])
                    )
                )
            photo_face_path = search(
                os.path.join(
                    'Соц.Сети',
                    '{}'.format(objs[obj]['Адрес']),
                    'Морда.jpeg'
                    )
                )
            dist_path_photo = os.path.abspath(
                search(
                    os.path.join(
                        home_dir,
                        'static',
                        'images',
                        'Объекты',
                        '{}'.format(objs[obj]['Адрес'])
                        )
                    )
                )

            # if not os.path.exists(photo_face_path):
            shutil.copy(photo_face_path, dist_path_photo)
            
            for dirs in pathlib.Path(photo_path).iterdir():
                if dirs.is_dir():
                    files = [file for file in pathlib.Path(dirs).iterdir() if file.stat().st_size > 0 and file.exists()]

                    if 'Нефильтрованное' not in dirs.name:
                        for photo in files[0 : len(files) // 2 + 1 : 2]:
                            # print(photo)
                            shutil.copy(photo, dist_path_photo)
                    else:
                        for photo in files:
                            # print(photo)
                            shutil.copy(photo, dist_path_photo)

Basic.check_dirs(list_of_dirs)
Info.copy_bd(objs)
Info.copy_photo(objs, team)