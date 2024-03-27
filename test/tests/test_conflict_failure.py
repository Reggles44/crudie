import pytest
from tests import run_test, SERVICES


@pytest.mark.parametrize("service", SERVICES)
def test_update(service):
    run_test(
        service=service,
        path="update",
        method="PUT",
        headers={"Content-Type": "application/json"},
        status_code=409,
        expected={"service_key": service, "data": 2},
        json={"service_key": service, "data": 2},
    )


@pytest.mark.parametrize("service", SERVICES)
def test_delete(service):
    run_test(
        service=service,
        path="update",
        method="DELETE",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        status_code=409,
        expected={"service_key": service, "data": 2},
        params={"service_key": service},
    )
