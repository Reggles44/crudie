import sys
import json
import pytest
import requests

MODULE = sys.modules[__name__]
session = requests.Session()
session.trust_env = False


def backend_url(service, path):
    url = f"http://crudie-{service}-1:8000"
    for arg in path:
        url += f"/{arg}"
    return url


def handle_response(response):
    try:
        response.raise_for_status()
    except:
        print(json.dumps(response.json(), indent=4, default=str))


def create(path):
    data = {"service_key": path, "data": 1}
    url = backend_url(path, ['create', ])
    response = session.post(url, json=data)
    handle_response(response)
    response_data = response.json()
    assert isinstance(response_data.pop('id'), int)
    assert response_data == data


def read(path):
    data = {"service_key": path}
    url = backend_url(path, ["read", ])
    response = session.get(url, params=data)
    handle_response(response)
    response_data = response.json()
    assert isinstance(response_data.pop('id'), int)
    assert response_data == {**data, "data": 1} 


def update(path):
    data = {"service_key": path, "data": 2}
    url = backend_url(path, ["update", ])
    response = session.put(url, json=data)
    handle_response(response)
    response_data = response.json()
    assert isinstance(response_data.pop('id'), int)
    assert response_data == data 


def delete(path):
    data = {"service_key": path}
    url = backend_url(path, ["delete", ])
    response = session.delete(url, params=data)
    handle_response(response)
    response_data = response.json()
    assert isinstance(response_data.pop('id'), int)
    assert response_data == {**data, "data": 2} 


DEFAULT_SERVICES = [
    "python-fastapi-sql",
    "python-flask-sql",
    "python-django-sql",
]
for service in DEFAULT_SERVICES:

    @pytest.mark.parametrize("func", [create, read, update, delete])
    def run(func):
        func(service)

    setattr(MODULE, f"test_{service.replace('-', '_')}", run)


def test_if_tests_exist():
    base_tests = ["test_if_tests_exist", "test_duplicate_name"]
    dynamic_tests = [
        var for var in dir(MODULE) if var.startswith("test_") and var not in base_tests
    ]
    assert len(dynamic_tests) > 0, dynamic_tests
