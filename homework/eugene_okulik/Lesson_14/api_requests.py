import requests
import json


def get_all_posts():
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts').json()
    print(response[0])


def get_one_post():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/200')
    print(response.json())
    print(response.status_code)


def add_post():
    header = {
        'Content-Type': 'application/json',
    }
    data = {
        "title": "ksjhgdksjdfhksjdfhsd",
        "body": "skdjhfksjdfhksjdfh",
        "userId": 22
    }
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=data,
        headers=header
    ).json()
    print(response)


def put_post():
    header = {
        'Content-Type': 'application/json',
    }
    data = {
        "title": "ksjhgdksjdfhksjdfhsdUPD",
        "body": "skdjhfksjdfhksjdfhUPD",
        "userId": 25
    }
    response = requests.put(
        'https://jsonplaceholder.typicode.com/posts/42',
        json=data,
        headers=header
    ).json()
    print(response)


def patch_post():
    header = {
        'Content-Type': 'application/json',
    }
    data = {
        "title": "ksjhgdksjdfhksjdfhsdPATCH"
    }
    response = requests.patch(
        'https://jsonplaceholder.typicode.com/posts/42',
        json=data,
        headers=header
    ).json()
    print(response)


def delete_post():
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/42').json()
    print(response)


get_one_post()
