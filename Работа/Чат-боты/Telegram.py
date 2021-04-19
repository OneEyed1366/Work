import os, glob, telebot
from json import load, dump
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from Alarmer import alarm
from pathlib import Path

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

#Получаем токен бота
with open(
    search(
        os.path.join(
            'Данные для работы',
            'Боты',
            'Telegram',
            'Публичный.txt'
            )
        ), encoding='utf-8'
    ) as f:
        bot_token = f.read()

bot = telebot.AsyncTeleBot(bot_token)
go_on = True
#Глобальные переменные
target = ''
fake_target = ""
law_target = ''
target_type = ''
obj_type = ''
#Переменные для Каталога
objs = []
used_objs = []
homes = []
flats = []
chambers = [] 
commercial = []

with open(
    search(
        os.path.join(
            'Данные для работы',
            'Социалочка',
            'Наши услуги.json'
            )
            ), encoding='utf-8'
        ) as f:
            bd_services = load(f)


with open(
    search(
        os.path.join(
            'Данные для работы',
            'Социалочка',
            'Наши ресурсы.json'
            )
            ), encoding = 'utf-8'
        ) as f:
            bd_we = load(f)

#Универсальные кнопки
btn_back = InlineKeyboardButton('Назад')
btn_cat_all_types_inf = InlineKeyboardButton('Другая информация')
btn_home = InlineKeyboardButton('Все наши услуги')
btn_types_obj = InlineKeyboardButton('Типы объектов')
btn_contact_agent = InlineKeyboardButton('Связаться с Агентом')
btn_contact_law = InlineKeyboardButton('Связаться с Юристом')
btn_law_services = InlineKeyboardButton('Все юридические услуги')
# Словари
cat_types = {
    "Комнаты": "Комната",
    "Квартиры": "-к",
    "Дома": "Дом",
    "Коммерческая недвижимость": "Коммерческая"
}
#Списки
home_list = [
    'Каталог объектов',
    # 'Юридические услуги',
    'О нас'
    ]
about_list = [
    'Как Вас найти?',
    'У Вас есть сайт?',
    'Когда Вы работаете?', 
    'Какие услуги Вы оказываете?'
    ]
our_service_law_list = [
    'Составление договоров в простой письменной форме',
    'Оформление наследства',
    'Оформление Ипотечных сделок',
    'Оформление сделок с использованием Материнского Капитала',
    'Узаконение перепланировок Квартир/Домов',
    'Перевод помещения из Жилого в Нежилое',
    'Установление границ земельного Участка',
    'Раздел объекта на 2 самостоятельных',
    'Займы под Материнский Капитал'
    ]
our_service_law_info_list = [
    'В каком случае Вам это необходимо?',
    'Чьё присутствие необходимо?',
    'Необходимые документы',
    'Примерная стоимость',
    'Примерный срок выполнения',
    ]
cat_obj_info_list = [
    'Описание',
    'Цена',
    'Чертёж', 
    'Фото', 
    'Ссылки', 
    'Место на карте'
    ]
cat_obj_info_links_list = [
    'YouTube', 
    'Авито', 
    'ВК', 
    'OK',
    'Instagram'
    ]
cat_exept_list = [
    cat_obj_info_list,
    cat_obj_info_links_list
    ]
#Начальный экран - клавиатуры
(keyb_home, keyb_about_main, keyb_law_services, keyb_law_services_info, 
    keyb_cat_types_objs, keyb_cat_obj_info, keyb_cat_obj_info_links, 
    keyb_cat_commercial, keyb_cat_chambers, keyb_cat_flats, keyb_cat_homes) = (
    ReplyKeyboardMarkup(resize_keyboard=True) for _ in range(11))

for service in home_list:
    keyb_home.row(service)
#О нас - клавиатуры
keyb_about_main.row(btn_home)
keyb_about_main.row(btn_contact_agent, btn_contact_law)
for service in about_list:
    keyb_about_main.row(service)
#Юридические услуги - клавиатуры
keyb_law_services.row(btn_home, btn_contact_law)
for service in our_service_law_list:
    keyb_law_services.row(service)
    
keyb_law_services_info.row(btn_contact_law)
keyb_law_services_info.row(btn_home, btn_law_services)
for service in our_service_law_info_list:
    keyb_law_services_info.row(service)
#Каталог - клавиатуры
keyb_cat_types_objs.row(btn_home)
keyb_cat_types_objs.row(
    InlineKeyboardButton('Комнаты'),
    InlineKeyboardButton('Квартиры'),
    InlineKeyboardButton('Дома')
    )
keyb_cat_types_objs.row(
    InlineKeyboardButton('Коммерческая недвижимость')
    )

keyb_cat_obj_info.row(
    btn_home,
    btn_back,  
    btn_types_obj)
keyb_cat_obj_info.row(
    btn_contact_agent,
    btn_contact_law
    )
for service in cat_obj_info_list:
    keyb_cat_obj_info.row(service)

keyb_cat_obj_info_links.row(
    btn_home,
    btn_cat_all_types_inf, 
    btn_types_obj)
for type in cat_obj_info_links_list:
    keyb_cat_obj_info_links.row(type)

for keyboard in [keyb_cat_commercial, keyb_cat_chambers, keyb_cat_flats, keyb_cat_homes]:
    keyboard.row(btn_home, btn_types_obj)

@bot.message_handler(commands=["start"])
def start(msg):        
    bot.send_message(
        msg.chat.id, 
        'Здравствуйте, {}!\nЧем я могу Вам помочь? 🙂'.format(msg.from_user.first_name),
        reply_markup=keyb_home)
        
@bot.message_handler(content_types=['text'])
def chat_text(msg):
#Задаём глобальные переменные
    global scheduler, users, target, law_target, fake_target, target_type, obj_type
# Проверяем, пользовались ли нашим ботом ранее
    try:
        with open (
            Path().joinpath(
                "Данные для работы",
                "Боты",
                "Пользователи.json"
            ), "r+", encoding="utf-8"
        ) as f:
            users = load(f)
    except:
        users = {}
    
    if str(msg.from_user.id) not in users:
        with open (
            Path().joinpath(
                "Данные для работы",
                "Боты",
                "Пользователи.json"
            ), "w+", encoding="utf-8"
        ) as f:
            users[msg.from_user.id] = msg.from_user.username

            dump(users, f)

        alarm(os.path.basename(__file__), f"Увеличение числа пользователей бота.\nНовый пользователь: {msg.from_user.username}\n\nОбщее число: {len(users)}")


# Добавляем кнопки на клавиатуры
    # for key in cat_types:
    #     for obj in sorted(scheduler):
    #         if cat_types[key] in obj and (
    #             cat_types[key] not in keyb_cat_types_objs.to_json()
    #         ):
    #             keyb_cat_types_objs.row(InlineKeyboardButton(key))

    #             break
    # print(keyb_cat_types_objs.to_json())
    with open(
        search(
            os.path.join(
                'Данные для работы',
                'Социалочка',
                'Каталог.json')
                ), encoding='utf-8') as f:
                    scheduler = load(f)

    for obj in sorted(scheduler):
        if obj not in objs:
            if "Коммерческая" in obj:
                keyb_cat_commercial.row(obj)
            elif "Комната" in obj:
                keyb_cat_chambers.row(obj)
            elif "-к" in obj:
                keyb_cat_flats.row(obj)
            elif "Дом" in obj:
                keyb_cat_homes.row(obj)
            
            objs.append(obj)
#Задаём пути для получения файлов
    text_path = os.path.join(
        'Данные для работы',
        'Авито',
        '{}.txt'.format(target)
        )
    photo_path = os.path.join(
        'Соц.Сети',
        '{}'.format(target),
        'VK',
        'Фото')
    scheme_path = os.path.join(
        'Данные для работы',
        'Фотобанк',
        '{}'.format(target),
        'Чертеж_'
        )
    link_path = os.path.join(
        'Данные для работы',
        'Социалочка',
        'Ссылки',
        )
    bd_path = os.path.join(
        'Данные для работы',
        'БД',
        '{}.json'.format(target)
    )
    
#Переход на начальный экран
    if msg.text == 'Все наши услуги':
        bot.send_message(
            msg.chat.id, 
            'Хорошо! Вот, что я могу сделать 🙂',
            reply_markup=keyb_home
            )
#Запрос контактов
    if (msg.text == 'Связаться с Агентом'):
        bot.send_message(
            msg.chat.id,
            'Конечно! Отправляю контактные данные Агента...'
            )
        bot.send_contact(
            msg.chat.id,
            bd_we['Телефоны']['Агент'],
            'Андрей'
            )
    
    elif (msg.text == 'Связаться с Юристом'):
        bot.send_message(
            msg.chat.id,
            'Поняла! Отправляю контактные данные Юриста...'
            )
        bot.send_contact(
            msg.chat.id,
            bd_we['Телефоны']['Юрист'],
            'Ирина',
            'Геннадьевна'
            )
#Юридические услуги
    if msg.text in our_service_law_info_list and law_target == '':
        bot.send_message(
            msg.chat.id,
            'Ой-ей, я забыла, о чём Вы спрашивали!\n{}, можете напомнить? 🥺'.format(
                msg.from_user.first_name),
                reply_markup=keyb_law_services
            )
    else:
        if msg.text in our_service_law_list:
            if msg.text not in our_service_law_info_list:
                law_target = msg.text
        
        
    if msg.text == 'Юридические услуги':
        bot.send_message(
            msg.chat.id,
            'Конечно!\nЧто именно Вас интересует? 🙂',
            reply_markup=keyb_law_services
            )
    elif msg.text == 'Все юридические услуги':
        bot.send_message(
            msg.chat.id,
            '{}, что именно Вас интересует? 🙂'.format(
                msg.from_user.first_name),
            reply_markup=keyb_law_services
            )
    elif msg.text in our_service_law_list:
        if law_target in bd_services['Юридические услуги']:
            bot.send_message(
                msg.chat.id,
                'Поняла! Выберите интересующую Вас информацию',
                reply_markup=keyb_law_services_info
                )
        else:
            bot.send_message(
                msg.chat.id,
                'Ой! Приносим свои извинения, информация по данной теме потерялась! 🥺\nПостараемся исправить в ближайшее время'
                )
    elif msg.text in our_service_law_info_list and law_target:
        if msg.text in bd_services['Юридические услуги'][law_target]:
            bot.send_message(
                msg.chat.id,
                'Поняла! 🙂 Отпраляю необходимую информацию\n\nТема вопроса: {}\nВопрос: {}\n\nОтвет: {}'.format(
                    law_target,
                    msg.text,
                    bd_services['Юридические услуги'][law_target][msg.text])
                )
        else:
            bot.send_message(
                msg.chat.id,
                'Ой! Приносим свои извинения, информация по данному вопросу потерялась! 🥺\nПостараемся исправить в ближайшее время'
                )
#О нас
    if msg.text == 'О нас':
        bot.send_message(
           msg.chat.id,
           '{}, что бы Вы хотели узнать? 🙂'.format(
               msg.from_user.first_name),
           reply_markup=keyb_about_main
           )
    elif msg.text == 'Как Вас найти?':
        bot.send_message(
            msg.chat.id,
            'Мы находимся по адресу:\nВоронежская область, г.Россошь, ул.Пролетарская 120/2\nНа торце дома написано: Семейное АН "Прокопенко и Сын"\n\nОстановки:\n--кафе "Осень"\n--общежитие "Строитель"\n\nВход со двора'
            )
        bot.send_location(
            msg.chat.id,
            '50.1900493',
            '39.5772645'
            )
    elif msg.text == 'Когда Вы работаете?':
        bot.send_message(
            msg.chat.id,
            'Мы работаем с Понедельника по Пятницу, с 08:30 до 17:00\n\nКонсультации проводятся по предварительной записи. Чтобы записаться на прием - нажмите кнопку "Связаться с Юристом"'
            )
        bot.send_message(
            msg.chat.id,
            'Показы объектов Потенциальным Покупателям проводятся по предваритильной записи, в заранее оговоренное время. Чтобы записаться на Просмотр - нажмите кнопку "Связаться с Агентом"'
            )
    elif msg.text == 'Какие услуги Вы оказываете?':
        bot.send_message(
            msg.chat.id,
            'Мы оказываем Посреднические и Юридические услуги по вопросам, так или иначе связанным с Недвижимостью\nСреди самых распространенных услуг - помощь при Продаже объекта, Поиск объектов по данным Заказчика, сопровождение Сделки КП (С/Без использования Ипотеки/Материнского Капитала)\nДля получения более подробной информации выберите интересующую Вас услугу из пункта "Юридические услуги" на начальном экране чат-бота'
            )
    elif msg.text == 'У Вас есть сайт?':
        bot.send_message(
            msg.chat.id,
            'Конечно! Отправляю Вам ссылку на наш сайт. Там Вы сможете ознакомиться с нашей картотекой, узнать об оказываемых нами услугах, а также больше узнать о нашей организации. 🙂\n{0}'.format(
                bd_we['Сайт'])
            )

#Каталог        
    if msg.text in objs: 
        target = scheduler[msg.text]['Адрес']
        fake_target = msg.text
        
        bot.send_message(
            msg.chat.id,
            'Хорошо! Какая информация Вам нужна? 🙂',
            reply_markup=keyb_cat_obj_info)
            
    elif (target or obj_type) == '' and (
        msg.text in (
            cat_obj_info_list or cat_obj_info_links_list)):
                bot.send_message(
                    msg.chat.id,
                    'Ой! {}, я забыла, с чем Вы работали!\nМожете напомнить? 🥺'.format(
                        msg.from_user.first_name),
                    reply_markup=keyb_cat_types_objs)
                    
                obj_type = msg.text
                    
    else:
        if msg.text == 'Каталог объектов':
            bot.send_message(
                msg.chat.id, 
                '{}, какого рода объекты Вас интересует? 🙂'.format(
                    msg.from_user.first_name),
                reply_markup=keyb_cat_types_objs)                     
            
        elif msg.text == 'Типы объектов':
            bot.send_message(
                msg.chat.id, 
                '{}, какого рода объекты Вас интересует? 🙂'.format(
                    msg.from_user.first_name),
                reply_markup=keyb_cat_types_objs)
        
        elif msg.text == 'Комнаты':
            obj_type = msg.text
                
            bot.send_message(
                msg.chat.id, 
                'Так, поняла! Комнаты! Вот, что у нас есть',
                reply_markup=keyb_cat_chambers)
            
        elif msg.text == 'Квартиры':
            obj_type = msg.text
            
            bot.send_message(
                msg.chat.id, 
                'Квартиры? Поняла! Вот, что у нас есть',
                reply_markup=keyb_cat_flats)
        
        elif msg.text == 'Дома':
            obj_type = msg.text
            
            bot.send_message(
                msg.chat.id, 
                'Ага, значит Дома! Вот, что у нас есть',
                reply_markup=keyb_cat_homes)
        
        elif msg.text == 'Коммерческая недвижимость':
            obj_type = msg.text
            
            bot.send_message(
                msg.chat.id, 
                'Ого! Коммерция! Вот, что у нас есть',
                reply_markup=keyb_cat_commercial)
            
        else:
            if msg.text == 'Назад' and obj_type:                
                if obj_type == 'Комнаты':
                    target_type = keyb_cat_chambers
                elif obj_type == 'Квартиры':
                    target_type = keyb_cat_flats
                elif obj_type == 'Дома':
                    target_type = keyb_cat_homes
                elif obj_type == 'Коммерческая недвижимость':
                    target_type = keyb_cat_commercial
                     
                bot.send_message(
                    msg.chat.id,
                    'Конечно! Вот {} 🙂'.format(obj_type),
                    reply_markup=target_type
                    )
            
            elif (msg.text == 'Цена') and target:
                if scheduler[fake_target]['Цена']:
                    price = scheduler[fake_target]['Цена']
                            
                    bot.send_message(
                        msg.chat.id,
                        'Конечно! 🙂 Сейчас отправлю цену...\n\nОбъект: {}\n\nЦена: {} руб.'.format(
                            fake_target,
                            price
                            )
                        )
                    
                else:
                    bot.send_message(
                        msg.chat.id,
                        'Ой-ей! Приношу извинения, данные о Цене потерялись!\nПостараемся исправить в ближайшее время 😅🙈'
                        )
                            
            
            elif (msg.text == 'Другая информация') and target:
                bot.send_message(
                    msg.chat.id,
                    'Хорошо! Какая информация Вам нужна? 🙂',
                    reply_markup=keyb_cat_obj_info)
            
            elif (msg.text == 'Описание') and target:         
                if search(text_path):
                    with open(
                        search(text_path),
                        encoding='utf-8') as f:
                            bot.send_message(
                                msg.chat.id, 
                                'Конечно!\n\nОбъект: {0}\n\n{1}'.format(
                                    fake_target,
                                    f.read()),
                                    reply_markup=keyb_cat_obj_info)
                else:
                    bot.send_message(
                        msg.chat.id, 
                        'Ой, приношу извинения! По данному объекту у нас потерялось описание... Выберите что-нибудь другое!',
                        reply_markup=keyb_cat_obj_info)
                        
            elif (msg.text == 'Фото') and target:
                if (search(photo_path)) and (os.listdir(search(photo_path))):
                    bot.send_message(
                        msg.chat.id,
                        'Поняла! Сейчас отправлю фотографии...\n\nОбъект: {}'.format(fake_target))
                        
                    for photo in glob.glob(
                        os.path.join(
                            search(photo_path),
                            '*')):
                            with open(photo, 'rb') as f:
                                bot.send_photo(
                                    msg.chat.id,
                                    f.read())
                            
                else:
                    bot.send_message(
                        msg.chat.id,
                        'Ой, приносим извинения! По данному объекту фотографии потерялись... Попробуйте выбрать что-нибудь другое!',
                        reply_markup=keyb_cat_obj_info)
                
            elif (msg.text == 'Ссылки') and target:
                bot.send_message(
                    msg.chat.id,
                    'Хорошо! Итак, какую именно ссылку нужно? 🥺',
                    reply_markup=keyb_cat_obj_info_links
                    )
            elif (msg.text in cat_obj_info_links_list) and target:
                if search(
                    os.path.join(
                        link_path,
                        '{}'.format(msg.text),
                        '{}.txt'.format(target))):
                            with open(
                                search(
                                    os.path.join(
                                        link_path,
                                        '{}'.format(msg.text),
                                        '{}.txt'.format(target))),
                                        encoding='utf-8') as f:
                                                    bot.send_message(
                                                        msg.chat.id,
                                                        'Конечно. 🙂\n\nОбъект: {0}\nСсылка на {1}\n{2}'.format(
                                                            fake_target,
                                                            msg.text,
                                                            f.read()),
                                                        reply_markup=keyb_cat_obj_info_links)
                    
                else:
                    bot.send_message(
                        msg.chat.id,
                        'Ой! Приносим извинения, данного объекта еще нет в {}! Постараемся исправить в ближайшее время...'.format(msg.text),
                        reply_markup=keyb_cat_obj_info_links)
                                        
            elif (msg.text == 'Чертёж') and target:
                if (search(scheme_path)) and (os.listdir(search(scheme_path))):
                    bot.send_message(
                        msg.chat.id,
                        'Конечно! Отправляю чертёж...\n\nОбъект: {}'.format(fake_target))
                        
                    for photo in glob.glob(
                        os.path.join(
                            search(scheme_path),
                            '*')):
                                with open(photo, 'rb') as f:
                                    bot.send_photo(
                                        msg.chat.id,
                                        f.read())
                            
                else:
                    bot.send_message(
                        msg.chat.id,
                        'Ой, приносим извинения! По данному объекту чертёж недоступен! Постараемся исправить в ближайшее время!..',
                        reply_markup=keyb_cat_obj_info)
                        
            elif (msg.text == 'Место на карте') and target:
                if (search(bd_path)):
                    with open(
                        search(bd_path), 
                        encoding='utf-8') as f:
                            location = load(f)
                            
                    if (
                        location['Широта'] or location['Долгота']) != '0' and (
                            location['Широта'] or location['Долгота']) != '':
                                bot.send_message(
                                    msg.chat.id,
                                    'Хорошо! Сейчас отправлю геопозицию...\n\nОбъект: {}'.format(
                                        fake_target
                                    )
                                )
                                
                                bot.send_location(
                                    msg.chat.id,
                                    location['Широта'],
                                    location['Долгота'],
                                    reply_markup=keyb_cat_obj_info
                                    )
                    else:
                        bot.send_message(
                            msg.chat.id,
                            'Ой! Приносим извинения, у данного объекта некорректно отображается геопозиция!\nПостараемся исправить в ближайшее время...',
                            reply_markup=keyb_cat_obj_info)

                else:
                    bot.send_message(
                        msg.chat.id,
                        'Ой! Приносим извинения, данные по расположению данного объекта потерялись!\nПостараемся исправить в ближайшее время!..',
                        reply_markup=keyb_cat_obj_info
                    )
                    

# try:
#     bot.polling(none_stop=True)
# except KeyboardInterrupt:
#     print("Закрываю чат-бота по инициативе пользователя! :)")
#     alarm(os.path.basename(__file__), "Закрываю чат-бота по инициативе пользователя! :)")
# except Exception as e:
#     print(f"Ошибка! ({e})")
#     alarm(os.path.basename(__file__), f"Ошибка!\n{e}")

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
