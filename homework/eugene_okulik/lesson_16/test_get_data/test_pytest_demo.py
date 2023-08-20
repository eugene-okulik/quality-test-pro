import pytest
import requests
from datetime import datetime


def test_get_all_posts(all_tests, base_url):
    response = requests.request('GET', f'{base_url}/posts')
    assert response.status_code == 200
    assert len(response.json()) == 100


@pytest.mark.parametrize('i', range(10))
def test_add_post(base_url, i):
    header = {
        'Content-Type': 'application/json',
    }
    data = {
        "title": "ksjhgdksjdfhksjdfhsd",
        "body": "skdjhfksjdfhksjdfh",
        "userId": 22
    }
    response = requests.post(
        f'{base_url}/posts',
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


def test_get_one_post(post_id, base_url):
    response = requests.get(f'{base_url}/posts/{post_id}')
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
