import requests
import json


def create_post():
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
    return response['id']


def cleanup(post_id):
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')


def get_all_posts():
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts')
    # print(response)
    assert response.status_code == 200, 'Status code is not OK'
    assert len(response.json()) == 101, 'API returned incorrect quantity of posts'


def get_one_post():
    post_id = create_post()
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    assert response.status_code == 200
    assert response.json()['id'] == post_id
    cleanup(post_id)


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
    post_id = create_post()
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    assert response.status_code == 404


# get_all_posts()
# get_one_post()
add_post()
# put_post()
# patch_post()
# delete_post()
