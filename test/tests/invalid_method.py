import pytest
from tests import test, DEFAULT_SERVICES


@pytest.mark.parametrize("service", DEFAULT_SERVICES)
def create(service):
    test(
        service=service,
        path="create",
        method="GET",
        status_code=405,
    )

@pytest.mark.parametrize("service", DEFAULT_SERVICES)
def read(service):
    test(
        service=service,
        path="read",
        method="POST",
        status_code=405,
    )


@pytest.mark.parametrize("service", DEFAULT_SERVICES)
def update(service):
    test(
        service=service,
        path="update",
        method="DELETE",
        status_code=405,
    )


@pytest.mark.parametrize("service", DEFAULT_SERVICES)
def delete(service):
    test(
        service=service,
        path="update",
        method="PUT",
        status_code=405,
    )
