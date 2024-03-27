import pytest
from tests import test, DEFAULT_SERVICES


@pytest.mark.parametrize("service", DEFAULT_SERVICES)
def create(service):
    test(
        service=service,
        path="create",
        method="POST",
        status_code=200,
        expected={"service_key": service, "data": 1},
        json={"service_key": service, "data": 1},
    )


@pytest.mark.parametrize("service", DEFAULT_SERVICES)
def read(service):
    test(
        service=service,
        path="read",
        method="GET",
        status_code=200,
        expected={"service_key": service, "data": 1},
        params={"service_key": service},
    )


@pytest.mark.parametrize("service", DEFAULT_SERVICES)
def update(service):
    test(
        service=service,
        path="update",
        method="PUT",
        status_code=200,
        expected={"service_key": service, "data": 2},
        json={"service_key": service, "data": 2},
    )


@pytest.mark.parametrize("service", DEFAULT_SERVICES)
def delete(service):
    test(
        service=service,
        path="update",
        method="DELETE",
        status_code=200,
        expected={"service_key": service, "data": 2},
        params={"service_key": service},
    )
