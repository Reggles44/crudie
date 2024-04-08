import pytest
from tests import run_test, SERVICES


@pytest.mark.parametrize("service", SERVICES)
def test_create(service):
    run_test(
        service=service,
        path="create",
        method="POST",
        headers={"Content-Type": "application/json"},
        status_code=406,
        json={"service": service, "data": 1},
    )


@pytest.mark.parametrize("service", SERVICES)
def test_read(service):
    run_test(
        service=service,
        path="read",
        method="GET",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        status_code=406,
        params={"service": service},
    )


@pytest.mark.parametrize("service", SERVICES)
def test_update(service):
    run_test(
        service=service,
        path="update",
        method="PUT",
        headers={"Content-Type": "application/json"},
        status_code=406,
        json={"service": service, "data": 2},
    )


@pytest.mark.parametrize("service", SERVICES)
def test_delete(service):
    run_test(
        service=service,
        path="delete",
        method="DELETE",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        status_code=406,
        params={"service": service},
    )

