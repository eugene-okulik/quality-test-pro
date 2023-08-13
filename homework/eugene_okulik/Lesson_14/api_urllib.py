from urllib import request
import json


def get_all_posts():
    req = request.Request('https://jsonplaceholder.typicode.com/posts')
    response = request.urlopen(req)
    # response = response.read().decode('utf-8')
    response = json.load(response)
    print(response[0])


def get_one_post():
    req = request.Request('https://jsonplaceholder.typicode.com/posts/200')
    response = request.urlopen(req)
    response = json.load(response)
    print(response)


def add_post():
    req = request.Request('https://jsonplaceholder.typicode.com/posts', method='POST')
    req.add_header('Content-Type', 'application/json')
    req.data = json.dumps({
        "title": "ksjhgdksjdfhksjdfhsd",
        "body": "skdjhfksjdfhksjdfh",
        "userId": 22
    }).encode('ascii')
    response = json.load(request.urlopen(req))
    print(response)


def put_update():
    req = request.Request('https://jsonplaceholder.typicode.com/posts/42', method='PUT')
    req.add_header('Content-Type', 'application/json')
    req.data = json.dumps({
        "title": "ksjhgdksjdfhksjdfhsdUPD",
        "body": "skdjhfksjdfhksjdfhUPD",
        "userId": 25
    }).encode('ascii')
    response = request.urlopen(req)
    print(response.getcode())
    response = json.load(response)
    print(response)


def patch_update():
    req = request.Request('https://jsonplaceholder.typicode.com/posts/42', method='PATCH')
    req.add_header('Content-Type', 'application/json')
    req.data = json.dumps({
        "title": "ksjhgdksjdfhksjdfhsdPATCH"
    }).encode('ascii')
    response = request.urlopen(req)
    print(response.getcode())
    response = json.load(response)
    print(response)


def delete_post():
    req = request.Request('https://jsonplaceholder.typicode.com/posts/42', method='DELETE')
    response = json.load(request.urlopen(req))
    print(response)


get_one_post()
