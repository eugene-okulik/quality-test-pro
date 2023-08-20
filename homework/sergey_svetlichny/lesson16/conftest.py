import pytest
import config

app_url = config.app_url

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

@pytest.fixture()
def base_url():
    return app_url