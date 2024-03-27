import pytest
from tests import run_test, SERVICES


@pytest.mark.parametrize("service", SERVICES)
@pytest.mark.parametrize("method", ["GET", "POST", "PUT", "DELETE"])
def test_invalid(service, method):
    run_test(
        service=service,
        method=method,
        path="test",
        status_code=404,
    )

