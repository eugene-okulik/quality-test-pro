import pytest
import os
from dotenv import load_dotenv

load_dotenv()

login = os.getenv('LOGIN')
passwd = os.getenv('PASSWORD')


@pytest.fixture()
def base_url():
    return 'local'


def test_g():
    print(login)
    print(passwd)
    assert 1 == 1


def test_h():
    assert 1 == 1


def test_base_url(base_url):
    print(base_url)
    assert 2 == 2
