# Офurl1=Noneсты из задания 14 как тесты, которые можно запустить с помощью Pytest.
# Тест на создание ссылки оформите так, чтобы он тестировал 3 разные ссылки с помощью parametrize
# Сделайте так, чтобы перед запуском всех тестов распечатывалось "Start testing", а по завершении всех тестов -
# "Testing completed"
# Сделайте так, чтобы перед каждым тестом распечатывалось "before test", а после каждого теста - "after test"
# Пометьте 1 тест как "critical", а один тест как "medium". Сделайте так, чтобы при выполнении тестов в терминале
# не было ошибок и ворнингов.

import pytest
import requests


@pytest.fixture()
def one_test():
    print('Before test')
    yield
    print('After test')


@pytest.fixture(scope='session')
def all_tests():
    print('Start testing')
    yield
    print('Testing completed')


def post_codes(url):
    header = {
        'Content-Type': 'application/json',
    }
    data = {
        "input": url  # "https://okulik.by/kabinet/group?groupId=2"
    }
    response = requests.post(
        'https://gotiny.cc/api',
        json=data,
        headers=header
    )
    p_code = response.json()[0]['code']
    return p_code
    # print('https://gotiny.cc/api/' + post_code)
    # assert response.status_code == 200


@pytest.mark.critical
def test_create_post_opt(all_tests, one_test):
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
    my_dict = response
    assert my_dict["error"]["message"] == 'Code already taken: amazon'


@pytest.mark.skip('for testing skipping')
def test_create_post_fallb(one_test):
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
    assert response[0]['long'] == 'https://amazon.com/very-long-url'


@pytest.mark.parametrize('url', ['https://okulik.by/kabinet/group?groupId=2',
                                 'https://amazon.com/long-url',
                                 'https://ya.ru'])
def test_link_get_text(url):
    p_cod = post_codes(url)
    response = requests.get(f'https://gotiny.cc/api/{p_cod}')
    assert response.text == url


@pytest.mark.medium
def test_link_get_json(one_test):
    response = requests.get('https://gotiny.cc/api/snh35s?format=json').json()
    assert response['long'] == 'https://okulik.by/kabinet/group?groupId=2'

# pytest -v -s -m 'not critical' - write this in terminal to run [wrote to not forget this :-)]
