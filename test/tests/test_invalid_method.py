import pytest
from tests import run_test, SERVICES


@pytest.mark.parametrize("service", SERVICES)
def test_create(service):
    run_test(
        service=service,
        path="create",
        method="GET",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        status_code=405,
    )

@pytest.mark.parametrize("service", SERVICES)
def test_read(service):
    run_test(
        service=service,
        path="read",
        method="POST",
        headers={"Content-Type": "application/json"},
        status_code=405,
    )


@pytest.mark.parametrize("service", SERVICES)
def test_update(service):
    run_test(
        service=service,
        path="update",
        method="DELETE",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        status_code=405,
    )


@pytest.mark.parametrize("service", SERVICES)
def test_delete(service):
    run_test(
        service=service,
        path="update",
        method="PUT",
        headers={"Content-Type": "application/json"},
        status_code=405,
    )
