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
class Basic():
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
            # else:
            #     os.rmdir(
            #         os.path.join(
            #             home_dir,
            #             'static',
            #             dir
            #             )
            #         )

            #     os.mkdir(
            #         os.path.join(
            #             home_dir,
            #             'static',
            #             dir
            #             )
            #         )
class Info():
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
            # pathlib.Path(dist_path_bd).rmdir()

            shutil.copy(bd_path, dist_path_bd)


    def copy_photo(objects):
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

            for dirs in pathlib.Path(photo_path).iterdir():
                files = []
                num = 0

                if dirs.is_dir():
                    for file in pathlib.Path(dirs).iterdir():
                        files.append(file)

                    if 'Нефильтрованное' not in dirs.name:
                        for photo in files[(len(files) // 4) : ((len(files) // 4) + 1)]:
                            shutil.copy(photo, dist_path_photo)
                    else:
                        for photo in files:
                            shutil.copy(photo, dist_path_photo)
                        # print(dist_path_photo)
                        # shutil.copy(file, dist_path_photo)
                        

Basic.check_dirs(list_of_dirs)
Info.copy_bd(objs)
Info.copy_photo(objs)
