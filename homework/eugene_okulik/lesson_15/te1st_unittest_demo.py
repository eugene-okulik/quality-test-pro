import unittest
import requests
import sys


class TestPostsApi(unittest.TestCase):
    post_id = None

    def setUp(self) -> None:
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
        self.post_id = response['id']

    def tearDown(self) -> None:
        requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')

    def test_get_one_post(self):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json()['id'], self.post_id)


class TestIndependent(unittest.TestCase):
    def test_get_all_posts(self):
        response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 100)

    def test_add_post(self):
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
        self.assertEqual(response.status_code, 201)
        response = response.json()
        self.assertEqual(response['title'], 'ksjhgdksjdfhksjdfhsd')
        self.assertEqual(response['body'], 'skdjhfksjdfhksjdfh')
        self.assertEqual(response['userId'], 22)

    @unittest.skip('Bug # 17232673')
    def test_a(self):
        self.assertEqual(1, 1)

    @unittest.skipIf(sys.platform.startswith('lin'), 'don\'t run this test on linux')
    def test_b(self):
        self.assertEqual(1, 1)


'''
assertEqual(a, b) — a == b
assertNotEqual(a, b) — a != b
assertTrue(x) — bool(x) is True
assertFalse(x) — bool(x) is False
assertIs(a, b) — a is b
assertIsNot(a, b) — a is not b
assertIsNone(x) — x is None
assertIsNotNone(x) — x is not None
assertIn(a, b) — a in b
assertNotIn(a, b) — a not in b
assertIsInstance(a, b) — isinstance(a, b)
assertNotIsInstance(a, b) — not isinstance(a, b)
assertGreater(a, b) — a > b
assertGreaterEqual(a, b) — a >= b
assertLess(a, b) — a < b
assertLessEqual(a, b) — a <= b
'''
