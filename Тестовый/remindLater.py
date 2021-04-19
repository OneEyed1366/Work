import re, dialogs, datetime, reminders, calendar

text = dialogs.text_dialog('Напиши в меня что-нибудь 🙂')
time_pattern = r'\b.{,2}?[0-9]?[0-9]:[0-9][0-9]'
day_pattern = r'\b.{,3}?понедельник\w?|\b.{,3}?вторник\w?|\b.{,3}?сред\w?|\b.{,3}?четверг\w?|\b.{,3}?пятниц\w?|\b.{,3}?суббот\w?|\b.{,3}?воскресень\w?|завтра|послезавтра|[0-9]?[0-9] [а-яА-ЯёЁ]{3,10}'
hashtag_pattern = r'#.+\b'

t_time = re.findall(time_pattern, text)
t_day = re.findall(day_pattern, text)
t_hashtag = re.findall(hashtag_pattern, text)
#Нужно сделать так, чтобы когда функция находила соответсвия, она их удаляла в исходном тексте
new_text = re.sub(text, time_pattern, text)

print('{0}-время, {1}-день, {2}-#, {3}-после удаления'.format(t_time, t_day, t_hashtag, new_text))
