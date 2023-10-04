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
        "long": "https://litres.ru/long-url",
        "custom": "litlit",
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
        "long": "https://litres.ru/long-url",
        "custom": "litlit",
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


print("task_1:")
post_code = create_post_my()[0]['code']
print('https://gotiny.cc/api/' + post_code)
print('task_2:')
print(create_post_opt())
print('task_3:')
print(create_post_fallb())
print('task_4:')
link_get_text()
print('task_5:')
link_get_json()
