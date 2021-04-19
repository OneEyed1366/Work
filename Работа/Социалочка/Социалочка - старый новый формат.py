import os, json, datetime, fileinput

#Задаем переменные
#Приходится помимо простого открытия файла форматировать его в список, при "нормальном" файле - пренебречь
with open('/private/var/mobile/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/Данные для работы/Социалочка/Группы/ОК.txt') as f:
    groups = str(f.read()).rsplit()

with open('/private/var/mobile/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/Данные для работы/Социалочка/График.json', encoding='utf-8') as f:
    scheduler = json.load(f)
    
with open('/private/var/mobile/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/Данные для работы/Социалочка/Адрес группы.txt', 'r') as f:
    our_group = f.readline()    

with open('Мемы-уже было.txt', 'a+') as f:
    memes_history = f.read()

with open('новости.txt', 'r+', encoding='utf-8') as f:
    news_to_post = f.readlines()

memes = os.listdir('/private/var/mobile/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/Данные для работы/Мемы/')
today = datetime.date.isoweekday(datetime.date.today())
objs = []
used_news = []
step_size_news = 10
step_size_mems = 50
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

#Функция, создающая список постов для каждого бота
def combine():
    number = 0
    
    with open('Ссылки 1.txt', 'w') as f:
        for obj in objs:
            for group in groups:
                count = 0
                l = open('/private/var/mobile/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/Соц.Сети/{}/Ссылки/OK.txt'.format(obj)).readline()
                
                f.write('{0} {1}\n'.format(group, l))
                number = number + 1
#Делаем проверку для каждого мема, если mem нет в memes_history, добавляем в файл
                for mem in memes:
                    if ((number % step_size_mems == 0) is True) and (mem not in memes_history):
                            
                        f.write('{0} {1}\n'.format(our_group, mem))
                        #m_history.write('{}\n'.format(mem))
                        
                        break
                
                for news in news_to_post:
                    if ((number % step_size_news == 0) is True) and (news not in used_news):
                        f.write('{0} {1}'.format(our_group, news))
                        used_news.append(news)
                        
                        break


when_check()
combine()
