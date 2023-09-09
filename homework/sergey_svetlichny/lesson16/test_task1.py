# В тесты, созданные в домашнем задании 15 внесите следующие изменения:
# Вынесите все фикстуры в отдельный файл conftest.py
# Сделайте так, чтобы основной урл апишки брался из конфигурационного файла, который не будет улетать в github
# Сделайте возможным параллельный запуск тестов в несколько потоков.

import pytest
import requests
import allure


# @pytest.fixture()
def post_codes(url, base_url):
    header = {
        'Content-Type': 'application/json',
    }
    data = {
        "input": url  # "https://okulik.by/kabinet/group?groupId=2"
    }
    response = requests.post(
        base_url,
        json=data,
        headers=header
    )
    p_code = response.json()[0]['code']
    return p_code
    # print('https://gotiny.cc/api/' + post_code)
    # assert response.status_code == 200


@allure.feature('Simple')
@allure.story('Posting')
@allure.title('Get all posts')
@allure.link('okulik.by')
@pytest.mark.critical
def test_create_post_opt(all_tests, one_test, base_url):
    with allure.step('Prepare headers'):
        header = {
            'Content-Type': 'application/json',
        }
    with allure.step('Prepare data'):
        data = {
            "long": "https://amazon.com/very-long-url",
            "custom": "amazon",
            "useFallback": False
        }
    with allure.step('Execute request'):
        response = requests.post(
            base_url,
            json=data,
            headers=header
        ).json()
    with allure.step('Assert that error is correct'):
        my_dict = response
        assert my_dict["error"]["message"] == 'Code already taken: amazon'


@allure.feature('Simple')
@pytest.mark.skip('for testing skipping')
def test_create_post_fallb(one_test, base_url):
    header = {
        'Content-Type': 'application/json',
    }
    data = {
        "long": "https://amazon.com/very-long-url",
        "custom": "amazon",
        "useFallback": True
    }

    response = requests.post(
        base_url,
        json=data,
        headers=header
    ).json()
    assert response[0]['long'] == 'https://amazon.com/very-long-url'


@allure.feature('Important')
@allure.story('Getting url')
@pytest.mark.parametrize('url', ['https://okulik.by/kabinet/group?groupId=2',
                                 'https://amazon.com/long-url',
                                 'https://ya.ru'])
def test_link_get_text(url, base_url):
    p_cod = post_codes(url, base_url)
    response = requests.get(f'{base_url}/{p_cod}')
    assert response.text == url


@allure.feature('Hard')
@allure.story('Getting posts')
@pytest.mark.medium
@pytest.mark.parametrize('i', range(10))
def test_link_get_json(one_test, base_url, i):
    response = requests.get(f'{base_url}/snh35s?format=json').json()
    assert response['long'] == 'https://okulik.by/kabinet/group?groupId=2'

# pytest -v -s -n 2 --reruns 2    - write this in terminal to run with 2 threads with 2 reruns
# pytest -v -s -n 2 --reruns 2 --alluredir=allure-results   - to make allure results
# allure serve    - to make report
