import os, csv, wget, requests
# Задаём переменные
posts_path = 'C:\\Users\\Андрей\\iCloudDrive\\iCloud~is~workflow~my~workflows\\Данные для работы\\Социалочка\\Посты\\Магазин\\Товары.txt'
csv_path = 'C:\\Users\\Андрей\\iCloudDrive\\iCloud~is~workflow~my~workflows\\Загрузки\\Dropo.csv'
photo_path = 'C:\\Users\\Андрей\\iCloudDrive\\iCloud~is~workflow~my~workflows\\Данные для работы\\Социалочка\\Посты\\Магазин\\Фото\\'

with open(posts_path, 'w+', encoding='utf-8') as f:
    with open(csv_path, 'r+', encoding='utf-8') as csv_file:
        for row in csv.DictReader(csv_file, delimiter=';'):
            if os.path.exists('{0}{1}.jpeg'.format(photo_path, row['Модель'])):
                pass
            else:
                if requests.get('{}'.format(row['Изображение']), verify=False).status_code == 200:
                    wget.download(
                        row['Изображение'],
                        '{0}{1}.jpeg'.format(photo_path, row['Модель'])
                        )

            f.write('{3}\\nБренд: {4}\\nМодель: {1}\\n\\nЦена: {2}\\n{0}\n'.format(
                '[image:{}]'.format('{0}{1}.jpeg'.format(
                    photo_path,
                    row['Модель'])),
                    row['Название'],
                    row['РРЦ'],
                    row['Описание'],
                    row['Бренд']
            ))   