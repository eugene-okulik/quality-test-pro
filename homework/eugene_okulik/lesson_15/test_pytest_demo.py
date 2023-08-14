import pytest
import requests
from datetime import datetime


@pytest.fixture()
def post_id():
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
    p_id = response['id']
    yield p_id
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{p_id}')


@pytest.fixture()
def one_test():
    print('Before test')
    yield
    print('After test')


@pytest.fixture(scope='session')
def all_tests():
    print('Before all')
    yield
    print('After all')


def test_get_all_posts(all_tests):
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200
    assert len(response.json()) == 100


def test_add_post():
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
    )
    assert response.status_code == 201
    response = response.json()
    assert response['title'] == 'ksjhgdksjdfhksjdfhsd'
    assert response['body'] == 'skdjhfksjdfhksjdfh'
    assert response['userId'] == 22


@pytest.mark.skip('feature is not implemented')
def test_a():
    assert 1 == 1


@pytest.mark.skipif(datetime.now().weekday() == 6, reason='don\'t work on sundays')
def test_b():
    assert 1 == 1


@pytest.mark.skipif(datetime.now().weekday() != 6, reason='works only on sundays')
def test_c():
    assert 1 == 1


def test_get_one_post(post_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['id'] == post_id


@pytest.mark.regression
def test_d(one_test):
    assert 1 == 1


def test_e(all_tests):
    assert 1 == 1


@pytest.mark.smoke
def test_f(one_test):
    assert 1 == 1


@pytest.mark.parametrize('login', ['ginger', 'luser1', 'admin'])
def test_login(login):
    print(login)
