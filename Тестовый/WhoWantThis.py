import json, io, os, dialogs

class BD:
    def compare():
        params = []   
        num_params = [
            {'title': 'Общая площадь:    ','type': 'number', 'key': 'whole'},
            {'title': 'Жилая площадь:    ', 'type': 'number', 'key': 'living'},
            {'title': 'Площадь кухни:    ','type': 'number', 'key': 'kitchen'}
            ]
        yes_no_params = [
            {'title': 'Комната?', 'type': 'switch', 'key': 'type-room'},
            {'title': 'Квартира?', 'type': 'switch', 'key': 'type-flat'},
            {'title': 'Дом?', 'type': 'switch', 'key': 'type-house'},
            {'title': 'Автономка?', 'type': 'switch', 'key': 'type-warm'}
            ]
        section = [
            ('Площади', num_params),
            ('Тип объекта', yes_no_params)
            ]
        wishes = dialogs.form_dialog('Параметры объекта для поиска', sections=section)

BD.compare()
