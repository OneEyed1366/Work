import os, glob, json, datetime, random, codecs, feedparser
from pathlib import Path
from sys import argv

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
#Задаем переменные
#Приходится помимо простого открытия файла форматировать его в список, при "нормальном" файле - пренебречь
with open(
    os.path.join(
        'Данные для работы',
        'Социалочка',
        'Группы',
        'ОК.txt')) as f:
            ok_groups = str(f.read()).rsplit()

with open(
    os.path.join(
        'Данные для работы',
        'Социалочка',
        'Группы',
        'ВК.txt')) as f:
            vk_groups = str(f.read()).rsplit()

with open(
    os.path.join(
        'Данные для работы',
        'Социалочка',
        'График.json'
        ), encoding='utf-8') as f:
            scheduler = json.load(f)

with open(
    os.path.join(
        'Данные для работы',
        'Социалочка',
        'Наши ресурсы.json'
        ), encoding = 'utf-8'
    ) as f:
        bd_we = json.load(f)

with open(
    os.path.join(
        'Данные для работы',
        'Социалочка',
        'Новости.txt'
        ), 'r') as f:
            news_to_post = f.readlines()
#Очень глупое решение. Если файл есть, просто закрываем. Если нет - создаем и закрываем
with open(
    os.path.join(
        'Данные для работы',
        'Социалочка',
        'Было',
        'OK.txt'
        ), 'a+') as f:
            f.close

with open(
    os.path.join(
        'Данные для работы',
        'Социалочка',
        'Было',
        'VK.txt'
        ), 'a+') as f:
            f.close

memes = glob.glob(
    os.path.join(
        'Данные для работы',
        'Мемы',
        'Готовые',
        '*'))
        

import os, feedparser

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
		'Список RSS каналов.txt'
		), 'r+', encoding="utf-8") as f:
			urls = f.read().split("\n")

with open(
	os.path.join(
		'Данные для работы',
		'Социалочка',
		'Новости-уже было.txt'
		), 'a+') as f:
			f.close()

def news_from_rss():
    result = []

    for url in urls:
        all_news = feedparser.parse(url)
        for news in all_news["entries"][ : 15]:
            if "tags" in news:
                try:
                    # try:
                    if ('недвиж' or 'realt') in news['tags'][0]['term'].lower():
                        # print(news.entries[news])
                        title = news.title
                        link = news.link
                        
                        try:
                            desc = news.summary
                        except AttributeError:
                            desc = news.description
                    
                    with open(
                        os.path.join(
                            'Данные для работы',
                            'Социалочка',
                            'Новости-уже было.txt'
                            ), 'r+') as news_history:
                                if title not in news_history.read():
                                    result.append(
                                        f'{title}\n\n\"{desc}\"\n\nСсылка на новость: {link}')

                                    news_history.write('{}\n'.format(title))

                except KeyError as key_e:
                    print(f"Ошибка: {key_e}")
                except IndexError as index_e:
                    print(f"Ошибка: {index_e}")
                except AttributeError as e:
                    print(f"Ошибка: {e}")
    return result

today = datetime.date.isoweekday(datetime.date.today())
objs = []
ok_used_news = []
vk_used_news = []
step_size_mems = 50
step_size_news = 30

#Проверка, есть ли в названии объекта ['ё', 'й']. Если есть - заменим на понятную python букву
def search_win(path):
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
    else:
        return ""
        
#Проверка, есть ли неиспользованные мемы. Если нет - удалить файл и постить их заново
def mems_check(social_network):
    mems = [Path(i).resolve().as_posix() for i in Path().joinpath(
        "Данные для работы", 
        "Мемы", 
        "Готовые").glob("*")]
    with open(os.path.join(
        'Данные для работы',
        'Социалочка',
        'Было',
        f"{social_network}.txt"
        ), "r+") as history:
            memes_history = history.readlines()
    # print(len(mems), len(memes_history))
    if len(memes_history) >= len(mems):
            with open(Path().joinpath(
                "Данные для работы",
                "Социалочка",
                "Было",
                f"{social_network}.txt"), "w+", encoding="utf-8") as f:
                    memes_history = []
    
    return [mem for mem in mems[ : 2] if mem not in memes_history]
            

#Функция, которая будет создавать описания объектов исходя из данных в БД
def text_creation():

    for obj in objs:
        with open(
            os.path.join(
                'Данные для работы',
                'БД',
                '{}.json'.format(obj)
                ), encoding='utf-8') as f:
                    bd = json.load(f)
                    print(bd['Стартовая цена'])

#Функция, получающая объекты, из которых нужно сделать посты
def when_check():
#Проверяем, какой сегодня день. Если он совпадает со значением ключа -> добавляем ключ в список
    for obj in scheduler:
        if (today == 1 and scheduler[obj] == 'Понедельник') or (
            today == 2 and scheduler[obj] == 'Вторник') or (
                today == 3 and scheduler[obj] == 'Среда') or (
                    today == 4 and scheduler[obj] == 'Четверг') or (
                        today == 5 and scheduler[obj] == 'Пятница') or (
                            today == 6 and scheduler[obj] == 'Суббота') or (
                                today == 7 and scheduler[obj] == 'Воскресенье'):

            objs.append(obj)

def inst_combine():
    number = 0
    
    with open(
        os.path.join(
            'Данные для работы',
            'Социалочка',
            'Посты',
            'Inst',
            'Постинг.txt'
            ), 'w+') as f:
                with open(
                    os.path.join(
                        'Данные для работы',
                        'Социалочка',
                        'Было',
                        'Instagram.txt'
                        ), 'r+') as m_history:
                            for mem in memes:
                                if (mem not in m_history.read()) and (number < 3):
                                    f.write(
                                        '[image:{0}]\n'.format(
                                            os.path.abspath(mem)
                                            )
                                        )
                                    m_history.write('{}\n'.format(mem))
                                    
                                    number = number + 1
                    
                                                            
def ok_combine():
#Запускаем "петлю", создающую файл для каждого бота в файле "Аккаунты.txt"
    with open(
        os.path.join(
            'Данные для работы',
            'Социалочка',
            'Аккаунты',
            'ОК',
            'Постинг.txt'
            ), 'r') as accs:
                number = 0
                bots_size = len(accs.readlines()) - 1
                max_on_bot = ((len(ok_groups) // bots_size) * len(objs)) // len(objs)
                ok_services = glob.glob(
                    os.path.join(
                        'Данные для работы',
                        'Социалочка',
                        'Текстовки',
                        'ОК',
                        'Услуги',
                        '*'
                        )
                    )
        #Путь файла с использованными мемами
                m_history_path = os.path.join(
                    'Данные для работы',
                    'Социалочка',
                    'Было',
                    'OK.txt'
                    )
                
                for acc in range(bots_size):
                    with open(
                        os.path.join(
                            'Данные для работы',
                            'Социалочка',
                            'Посты',
                            'ОК',
                            '{}.txt'.format(acc + 1)
                            ), 'w+') as f:
                                for group in ok_groups[number : (number + max_on_bot)]:
#Добавляем наши услуги из ok_services к каждой group
                                    for service in ok_services:
                                        with codecs.open(
                                            service, 
                                            'r+', 
                                            'utf-8'
                                            ) as f_service:
                                                f.write(
                                                    '{0} {1}\\n{2}\n'.format(
                                                        group, 
                                                        f_service.read(),
                                                        bd_we['Группы']['ОК']
                                                        )
                                                    )
#Формируем итоговый файл с постами
                                    for obj in objs:
                                        link_path = os.path.join(
                                            'Данные для работы',
                                            'Социалочка',
                                            'Ссылки',
                                            'OK',
                                            '{}.txt'.format(obj)
                                            )
                                        
                                        if search_win(link_path):
                                            link = open(search_win(link_path)).readline()
                                            f.write(
                                                '*{0} {1}\n'.format(
                                                    group, 
                                                    link
                                                    )
                                                )
                                        else:
                                            print('OK---Объект: {}, статус: не найдено'.format(obj))

                                        number = number + 1
#Добавляем новости в файл с постами. Если number кратен step_size_news, добавить новость в файл
                                        for news in news_to_post:
                                            if (news not in ok_used_news) and (number % step_size_news == 0):
                                                f.write(
                                                    '{0}\\n{1}'.format(
                                                        bd_we['Группы']['ОК'], 
                                                        news
                                                        )
                                                    )
                                                ok_used_news.append(news)

                                                break
#Добавляем мемы в файл. Если number кратен step_size_mems, то добавить мем в файл
                                        with open(m_history_path, 'r+') as m_history:
                                            for mem in memes:
                                                if (mem not in m_history.read()) and (number % step_size_mems == 0):
                                                    f.write(
                                                        '{0} [image:{1}]\n'.format(
                                                            bd_we['Группы']['ОК'], 
                                                            os.path.abspath(mem)
                                                            )
                                                        )
                                                    m_history.write('{}\n'.format(mem))

                                                    break

def vk_combine():
    number = 0
#Создаем новый файл с постами для ОК, затем - для каждого объекта получаем ссылку из файла и приписываем к каждой группе эту ссылку
    with open(
        os.path.join(
            'Данные для работы',
            'Социалочка',
            'Аккаунты',
            'ВК',
            'Постинг.txt'
            ), 'r') as accs:
                number = 0
                link = ''
                
                bots_size = len(accs.readlines()) - 1
                max_on_bot = ((len(vk_groups) // bots_size) * len(objs)) // len(objs)
                vk_services = glob.glob(
                    os.path.join(
                        'Данные для работы',
                        'Социалочка',
                        'Текстовки',
                        'ВК',
                        'Услуги',
                        '*'
                        )
                    )
#Путь файла с использованными мемами
                m_history_path = os.path.join(
                    'Данные для работы',
                    'Социалочка',
                    'Было',
                    'VK.txt'
                    )
                
                for acc in range(bots_size):
                    with codecs.open(
                        os.path.join(
                            'Данные для работы',
                            'Социалочка',
                            'Посты',
                            'ВК',
                            '{}.txt'.format(acc + 1)
                            ), 'w+', 'utf-8') as f:
                                for group in vk_groups[number : (number + max_on_bot)]:
#Добавляем наши услуги из vk_services в файл с постами
                                    #for service in vk_services:
                                        #with codecs.open(service, 'r+', 'utf-8') as f_service:
                                            #f.write('*{0} {1}\\n{2}\n'.format(group, f_service.read(), bd_we['ВК']))
#Формируем итоговый файл с постами                         
                                    for obj in objs:
#Пути файлов
                                        text_path = os.path.join(
                                            'Данные для работы',
                                            'Социалочка',
                                            'Текстовки',
                                            'ВК',
                                            '{}.txt'.format(obj)
                                            )
                                        photo_path = os.path.join(
                                            'Соц.Сети',
                                            '{}'.format(obj),
                                            'VK',
                                            'Фото',
                                            '*'
                                            ) 
                                        avito_path = os.path.join(
                                            'Данные для работы',
                                            'Социалочка',
                                            'Ссылки',
                                            'Авито',
                                            '{}.txt'.format(obj)
                                            )
                                        youtube_path = os.path.join(
                                            'Данные для работы',
                                            'Социалочка',
                                            'Ссылки',
                                            'YouTube',
                                            '{}.txt'.format(obj)
                                            )
                                        vk_path = os.path.join(
                                            'Данные для работы',
                                            'Социалочка',
                                            'Ссылки',
                                            'ВК',
                                            '{}.txt'.format(obj)
                                            )
#Исполнение скрипта                    
                                        photos = '{}'.format(
                                            ''.join(
                                                [str(
                                                    '[image:{}]'.format(
                                                        os.path.abspath(
                                                            photo))) for photo in glob.glob(
                                                                photo_path)]))

                                        if (search_win(youtube_path)) and (search_win(vk_path)):
                                            link = '{0}\\n\\n{1}'.format(
                                                open(search_win(youtube_path)).readline(), 
                                                open(search_win(vk_path)).readline())
                                        else:
                                            if (search_win(avito_path)) and (search_win(vk_path)):
                                                link = '{0}\\n\\n{1}'.format(
                                                    open(search_win(avito_path)).readline(),
                                                    open(search_win(vk_path)).readline())
                                                    
                                        if search_win(text_path):
                                            text = '{0}\\n\\n{1}'.format(
                                                codecs.open(
                                                    search_win(text_path),
                                                     'r+', 
                                                     'utf-8').read(), 
                                                link)
                                            f.write('*{0} {1}{2}\n'.format(
                                                group, 
                                                text, 
                                                photos
                                                )
                                            )
                                        else:
                                            print('ВК --> Объект: {}, статус: Не найден'.format(obj))
                                            
                                        number = number + 1
#Добавляем новости в файл с постами. Если number кратен step_size_news, добавить новость в файл
                                        for news in news_to_post:
                                            if (news not in vk_used_news) and (number % step_size_news == 0):
                                                f.write('{0} {1}'.format(
                                                    bd_we['Группы']['ВК'], 
                                                    news))
                                                vk_used_news.append(news)

                                                break
#Добавляем мемы в файл. Если number кратен step_size_mems, то добавить мем в файл
                                        with open(m_history_path, 'r+') as m_history:
                                            for mem in memes:
                                                if (mem not in m_history.read()) and (number % step_size_mems == 0):
                                                    f.write(
                                                        '{0} [image:{1}]\n'.format(
                                                            bd_we['Группы']['ВК'],
                                                            os.path.abspath(mem))
                                                        )
                                                    m_history.write('{}\n'.format(mem))

                                                    break
                                                    
def new_vk_combine():
    when_check()
    to_dump = {
        "news": news_from_rss(),
        "memes": mems_check("VK"),
        "objs": {}
    }
    number = 0
#Создаем новый файл с постами для ОК, затем - для каждого объекта получаем ссылку из файла и приписываем к каждой группе эту ссылку
    with open(
        os.path.join(
            'Данные для работы',
            'Социалочка',
            'Аккаунты',
            'ВК',
            'Постинг.txt'
            ), 'r') as accs:
                number = 0
                bots_size = len(accs.readlines()) - 1
                max_on_bot = ((len(vk_groups) // bots_size) * len(objs)) // len(objs)
                vk_services = glob.glob(
                    os.path.join(
                        'Данные для работы',
                        'Социалочка',
                        'Текстовки',
                        'ВК',
                        'Услуги',
                        '*'
                        )
                    )
                
                for acc in range(bots_size):
    #Добавляем наши услуги из vk_services в файл с постами
                        #for service in vk_services:
                            #with codecs.open(service, 'r+', 'utf-8') as f_service:
                                #f.write('*{0} {1}\\n{2}\n'.format(group, f_service.read(), bd_we['ВК']))
    #Формируем итоговый файл с постами                         
                    for obj in objs:
                        paths = {
                            "text": search_win(os.path.join(
                                "Соц.сети",
                                f"{obj}",
                                "Текст.txt"
                                )),
                            "photo": search_win(os.path.join(
                                'Соц.Сети',
                                f'{obj}',
                                'VK',
                                'Фото'
                                )),
                            "links": {
                                "avito": search_win(os.path.join(
                                    'Данные для работы',
                                    'Социалочка',
                                    'Ссылки',
                                    'Авито',
                                    f'{obj}.txt'
                                    )),
                                "youtube": search_win(os.path.join(
                                    'Данные для работы',
                                    'Социалочка',
                                    'Ссылки',
                                    'YouTube',
                                    f'{obj}.txt'
                                    )),
                                "vk": search_win(os.path.join(
                                    'Данные для работы',
                                    'Социалочка',
                                    'Ссылки',
                                    'ВК',
                                    f'{obj}.txt'
                                    ))
                            }
                        }                              
                        to_dump["objs"][obj] = {}
                        to_dump["objs"][obj]["photos"] = [os.path.abspath(photo) for photo in glob.glob(
                                                os.path.join(paths["photo"], "*"))]
                        with open(paths["text"], encoding="utf-8") as f:
                            to_dump["objs"][obj]["text"] = f.read()

                        for path in paths["links"]:
                            if os.path.exists(paths["links"][path]):
                                with open(paths["links"][path]) as new_f:
                                    to_dump["objs"][obj][path] = new_f.readline()
                        
                            
                        number += 1
                # print(to_dump)
                with codecs.open(
                    os.path.join(
                        'Данные для работы',
                        'Социалочка',
                        'Посты',
                        'ВК',
                        '{}.json'.format(acc + 1)
                    ), 'w+', encoding='utf-8') as f:
                    json.dump(to_dump, f)
# print(argv)
if len(argv) > 1:
    print(f"Скрипт: {argv[1]}")
    try:
        exec(f"{argv[1]}()")
    except:
        exec(f"{argv[1]}('{argv[2]}')")
else:
    when_check()
    # inst_combine()
    ok_combine()
    vk_combine()
