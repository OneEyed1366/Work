from ftplib import FTP
import os, glob, json, shutil

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

for obj in objs:
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

    dist_path = os.path.abspath(
        search(
            os.path.join(
                'Данные для работы',
                'Сайт',
                'bd'
                )
            )
        )

    for dir in os.listdir(photo_path):
        for file in os.listdir(search(os.path.join(photo_path, dir))):
            print(file)
    # shutil.copy(bd_path, dist_path)
