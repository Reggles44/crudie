import typing
import requests

session = requests.Session()
session.trust_env = False

DEFAULT_SERVICES = [
    "python-fastapi-sql",
    "python-flask-sql",
    "python-django-sql",
    "js-express-sql",
    "go-sql",
    "rust-sql",
]


def test(
    service: str,
    path: str,
    status_code: int,
    expected: typing.Optional[dict] = None,
    id_expected: bool = True,
    *args,
    **kwargs,
):
    url = f"http://crudie-{service}-1:8000/{path}"
    response = session.request(url, *args, **kwargs)
    assert response.status_code == status_code

    if expected:
        actual = response.json()
        assert id_expected and isinstance(actual.pop("id"), int)
        assert actual == expected
