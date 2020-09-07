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
    def check_files(paths):
        site_dirs = [dir for dir in pathlib.Path(os.path.join(home_dir, 'static', 'images', 'Объекты')).iterdir() if dir.is_dir()]

        for path in paths:

            original_dirs = [dir for dir in pathlib.Path().iterdir() if dir.is_dir()]

            print(original_dirs)
            
    # Создаём внутри корневого каталога сайта рабочие папки
    def check_dirs(dirs):
        for dir in dirs:
            if not os.path.exists(dir):
                os.mkdir(dir)
            else:
                shutil.rmtree(dir)
                os.mkdir(dir)
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

            shutil.copy(photo_face_path, dist_path_photo)
            
            for dirs in pathlib.Path(photo_path).iterdir():
                files = []

                if dirs.is_dir():
                    for file in pathlib.Path(dirs).iterdir():
                        if file.stat().st_size > 0 and file.exists():
                            files.append(file)
                        
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
# Basic.check_files(list_of_dirs)