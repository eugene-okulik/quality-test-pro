import pytest
import requests
from datetime import datetime
import allure


@allure.feature('Posts')
@allure.story('Get Posts')
@allure.title('Get all posts')
def test_get_all_posts(all_tests, base_url):
    response = requests.request('GET', f'{base_url}/posts')
    # b = 1 / 0
    assert response.status_code == 200
    assert len(response.json()) == 100


@allure.feature('Posts')
@allure.story('Create Posts')
@pytest.mark.parametrize('i', range(10))
def test_add_post(base_url, i):
    with allure.step('Prepare headers'):
        header = {
            'Content-Type': 'application/json',
        }
    with allure.step('Prepare data'):
        data = {
            "title": "ksjhgdksjdfhksjdfhsd",
            "body": "skdjhfksjdfhksjdfh",
            "userId": 22
        }
    with allure.step('Execute request'):
        response = requests.post(
            f'{base_url}/posts',
            json=data,
            headers=header
        )
    with allure.step('Check that status code is 201'):
        assert response.status_code == 201
    response = response.json()
    with allure.step('Check that title is correct'):
        assert response['title'] == 'ksjhgdksjdfhksjdfhsd'
    with allure.step('Check that body is correct'):
        assert response['body'] == 'skdjhfksjdfhksjdfh'
    with allure.step('Check that userId is correct'):
        assert response['userId'] == 22


@allure.feature('Simple')
@allure.story('Skipped')
@pytest.mark.skip('feature is not implemented')
def test_a():
    assert 1 == 1


@allure.feature('Simple')
@allure.story('Skipped')
@pytest.mark.skipif(datetime.now().weekday() == 6, reason='don\'t work on sundays')
def test_b():
    assert 1 == 1


@allure.feature('Simple')
@allure.story('Skipped')
@pytest.mark.skipif(datetime.now().weekday() != 6, reason='works only on sundays')
def test_c():
    assert 1 == 1


@allure.feature('Posts')
@allure.story('Get Posts')
def test_get_one_post(post_id, base_url):
    response = requests.get(f'{base_url}/posts/{post_id}')
    assert response.status_code == 404, 'Status code is incorrect'
    # assert response.json()['id'] == post_id


@allure.feature('Simple')
@allure.story('Equal')
@pytest.mark.regression
def test_d(one_test):
    assert 1 == 1


@allure.feature('Simple')
@allure.story('Equal')
def test_e(all_tests):
    assert 1 == 1


@allure.feature('Simple')
@allure.story('Equal')
@pytest.mark.smoke
def test_f(one_test):
    assert 1 == 1


@allure.feature('Simple')
@allure.story('Login')
@pytest.mark.parametrize('login', ['ginger', 'luser1', 'admin'])
def test_login(login):
    print(login)
