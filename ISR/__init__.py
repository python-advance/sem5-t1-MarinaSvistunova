'''
1.1. Исследовать функционал одного из модулей стандартной библиотеки (string, re, datetime, math, random, os, и т.д.)
     и, используя инструмент Jupyter Notebook, Typora, встроенный редактор Markdown сервиса GitHub, создать документ с
     описанием и примерами использования его функционала. Опубликовать его в портфолио.
1.2. Создание пользовательского пакета для приложения «Гостевая книга» («Регистрация на конференцию») с прототипами
     методов, позволяющих взаимодействовать с JSON-файлом (создание, удаление, переименование, чтение, запись).
     Формирование отчета по практическому заданию и публикация его в портфолио.
'''

# import json
#
# with open('sw_templates.json') as f:
#     templates = json.load(f)
#
# print(templates)
#
# for section, commands in templates.items():
#     print(section)
#     print('\n'.join(commands))
#

import json
import uuid

def singleton(cls):
    instances = {}

    def getinstance(*args):
        if cls not in instances:
            instances[cls] = cls(*args)
        return instances[cls]
    return getinstance


@singleton
class New_client:
    country = "Russia"

    def __init__(self):
        pass

    def clients_info(self):
        with open('ISR-1-2.json') as file:
            clients = json.load(file)
        print(json.dumps(clients, sort_keys=True, indent=4))
        return clients


    def get_client_info(self, first_name, second_name, city, index, address):

        client_id = uuid.uuid4()
        client_info = {
                        'first_name': first_name,
                        'second_name': second_name,
                        'country': self.country,
                        'city': city,
                        'index': index,
                        'address': address
        }

        to_json = self.clients_info()
        to_json[str(client_id)] = client_info

        with open('ISR-1-2.json', 'w') as file:
            json.dump(to_json, file)


    def print_client_info(self, id):
        from_json = self.clients_info()
        # print(json.dumps(from_json, sort_keys=True, indent=4))
        print(from_json[id])


    def delete_client(self, id):
        from_json = self.clients_info()
        for key in from_json.keys():
            key.pop(id, None)

    def upgrade_client(self, id, first_name=None, second_name=None, city=None, index=None, address=None):
        from_json = self.clients_info()
        one_client = from_json[id]

        information = {'first_name': first_name, 'second_name': second_name, 'city': city, 'index': index, 'address': address}
        for key, value in information.items():
            if value != None:
                one_client[key] = value

        from_json[id] = one_client
        with open('ISR-1-2.json', 'w') as file:
            json.dump(from_json, file)


base = New_client()
test_client = base.get_client_info('Konstatin', 'Konstantinopolskiy', 'Petropavlovsk-Kamchatsky', 683000, 'Vladivostokskaya, 35')
base.print_client_info(id='9a3f0a83-66cf-4143-95a0-e651fc381111')
base.delete_client(id='9a3f0a83-66cf-4143-95a0-e651fc381111')
base.clients_info()

# test_client2 = New_client('Seok Jin', 'Kim', 'Seoul', 3450, 'Gangnam')


# test_client.print_client_info()
# test_client.save_cards()
