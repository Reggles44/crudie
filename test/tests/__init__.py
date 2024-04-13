import typing
import requests

session = requests.Session()
session.trust_env = False

SERVICES = [
    "python-fastapi-sql",
    "python-flask-sql",
    "python-django-sql",
    "js-express-sql",
    "go-sql",
    "rust-sql",
]


def run_test(
    service: str,
    path: str,
    status_code: int,
    expected: typing.Optional[dict] = None,
    timeout=5,
    *args,
    **kwargs,
):
    url = f"http://crudie-{service}-1:8000/{path}"
    response = session.request(url=url, *args, **kwargs, timeout=timeout)
    print(response.status_code, response.content)
    assert response.status_code == status_code

    if expected:
        actual = response.json()
        assert isinstance(actual.pop("id"), int)
        assert actual == expected
