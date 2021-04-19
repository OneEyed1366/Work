import os, json, datetime, fileinput

#Задаем переменные
memes = os.listdir('/private/var/mobile/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/Данные для работы/Мемы/')    
today = datetime.date.isoweekday(datetime.date.today())
objs = []
step_size_mems = 50
step_size_news = 10
#Приходится помимо простого открытия файла убирать лишний \n, при "нормальном" файле - пренебречь
with open('/private/var/mobile/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/Данные для работы/Социалочка/Группы/ВК.txt') as f:
    groups = str(f.read()).rsplit()

with open('/private/var/mobile/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/Данные для работы/Социалочка/График.json', encoding='utf-8') as f:
    scheduler = json.load(f)
    
with open('/private/var/mobile/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/Данные для работы/Социалочка/Адрес группы.txt') as f:
    our_group = f.readline()    
#Очень глупое решение. Если файл есть, просто закрываем. Если нет - создаем и закрываем
with open('Мемы-уже было.txt', 'a+') as f:
    f.close
        
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
#Запускаем "петлю", создающую файл для каждого бота в файле "Аккаунты.txt"
    with open('Аккаунты.txt', 'r') as accs:
        count = 0
        bots_size = len(accs.readlines()) - 1
        max_on_bot = ((len(groups) // bots_size) * len(objs)) // len(objs)
        link = ''
        
        for acc in range(bots_size):
            with open('Ссылки {}.txt'.format(acc + 1), 'w+') as f:
                for group in groups[count : (count + max_on_bot)]:
                    count = count + 1
                    
                    for obj in objs:
                        link_path = os.path.join(
                            '/private/var/mobile/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/Данные для работы/Социалочка/Ссылки/OK', 
                            '{}.txt'.format(obj))
                            
                        if os.path.exists(link_path) == True:
                            link = open(link_path).readline()    
                            f.write('{0} {1}\n'.format(group, link))
                            
                            
                                            

when_check()
combine()
