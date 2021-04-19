import contacts, clipboard, datetime
import photos, dialogs, re, json

# Проверяем, есть ли пустые альбомы. Есть - удаляем
def assets_check():
    for asset in photos.get_albums():
        if not asset.assets:
            asset.delete()
                     
def watched():
    bd = json.load(clipboard.get())
    print(bd)
    phone = bd['Телефон']
    subject = bd['Заметка']
    when = bd['Дата']
    #phone = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', clipboard.get())
    #when = str(datetime.date.today())
# Проверяем, есть номер ли в буфере обмена. Есть - ищем в контактах совпадение
    for contact in contacts.get_all_people():
        for phones in contact.phone:
            if phone in phones:
                contact.note == "{0}: {1}".format(subject, when)
                contacts.save()
                clipboard.set("")
                dialogs.hud_alert("Сделано! 😉")



assets_check()
watched()
