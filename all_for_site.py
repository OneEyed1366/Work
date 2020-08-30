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
    'images',
    os.path.join('images', 'Объекты'),
    'bd',

]
class Info():
# Создаём внутри корневого каталога сайта рабочие папки
    def check_dirs(dirs):
        for dir in dirs:
            if not os.path.exists(
                os.path.join(
                    home_dir,
                    'static',
                    dir
                    )
                ):
                    os.mkdir(
                        os.path.join(
                            home_dir,
                            'static',
                            dir
                            )
                        )
# Копируем необходимую информацию в коневой каталог сайта
    def copy_inf(objects):
        for obj in objects:
            Info.check_dirs([
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

            bd_path = search(
                os.path.join(
                    'Данные для работы',
                    'БД',
                    '{}.json'.format(objs[obj]['Адрес'])
                    )
                )
            dist_path_bd = os.path.abspath(
                search(
                    os.path.join(
                        home_dir,
                        'static',
                        'bd'
                        )
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
# Копируем БД в dist_path_bd
            shutil.copy(bd_path, dist_path_bd)
# Копируем фотографии в dist_path_photo
            for dirs in pathlib.Path(photo_path).iterdir():
                if dirs.is_dir():
                    for file in pathlib.Path(dirs).iterdir():
                        # print(dist_path_photo)
                        shutil.copy(file, dist_path_photo)
                        

# Info.check_dirs(list_of_dirs)
Info.copy_inf(objs)
