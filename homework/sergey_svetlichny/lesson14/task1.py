# Для тестирования возьмем небольшое API сервиса сокращения ссылок: https://github.com/robvanbakel/gotiny-api
# Нужно простестировать все перечисленные в спецификации функции, а именно:
#
# Создание ссылки без дополнительных опций
# Создание ссылки с использованием опции custom (https://github.com/robvanbakel/gotiny-api#options)
# Создание ссылки с использованием опций custom и useFallback
# Получение длинной ссылки в виде текста (https://github.com/robvanbakel/gotiny-api#resolve-gotiny-link)
# Получение длинной ссылки в виде json
# Выполняйте всё задание так же, как я делал на занятии, - каждый запрос в отдельной функции.

import requests


def create_post_my():
    header = {
        'Content-Type': 'application/json',
    }
    data = {
        "input": "https://okulik.by/kabinet/group?groupId=2"
    }
    response = requests.post(
        'https://gotiny.cc/api',
        json=data,
        headers=header
    ).json()
    return response


def create_post_opt():
    header = {
        'Content-Type': 'application/json',
    }
    data = {
        "long": "https://amazon.com/very-long-url",
        "custom": "amazon",
        "useFallback": False
    }

    response = requests.post(
        'https://gotiny.cc/api',
        json=data,
        headers=header
    ).json()
    return response


def create_post_fallb():
    header = {
        'Content-Type': 'application/json',
    }
    data = {
        "long": "https://amazon.com/very-long-url",
        "custom": "amazon",
        "useFallback": True
    }

    response = requests.post(
        'https://gotiny.cc/api',
        json=data,
        headers=header
    ).json()
    return response


def link_get_text():
    # response = requests.get('https://gotiny.cc/api/snh35s?format=json').json()
    response = requests.get('https://gotiny.cc/api/snh35s')
    print(response.text)

def link_get_json():
    response = requests.get('https://gotiny.cc/api/snh35s?format=json').json()
    print(response)


print("first task:")
post_code = create_post_my()[0]['code']
print('https://gotiny.cc/api/' + post_code)
print('second task:')
print(create_post_opt())
print('third task:')
print(create_post_fallb())
print('fourth task:')
link_get_text()
print('fifth task:')
link_get_json()
