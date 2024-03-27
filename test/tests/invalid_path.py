import pytest
from tests import test, DEFAULT_SERVICES


@pytest.mark.parametrize("service", DEFAULT_SERVICES)
@pytest.mark.parametrize("method", ["GET", "POST", "PUT", "DELETE"])
def invalid(service, method):
    test(
        service=service,
        method=method,
        path="test",
        status_code=404,
    )

