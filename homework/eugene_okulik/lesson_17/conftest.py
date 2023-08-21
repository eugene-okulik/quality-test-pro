import pytest
import requests
import config

app_url = config.app_url


@pytest.fixture()
def post_id(base_url):
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
    ).json()
    p_id = response['id']
    yield p_id
    requests.delete(f'{base_url}/posts/{p_id}')


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


@pytest.fixture()
def base_url():
    return app_url
