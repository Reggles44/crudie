import pytest
from tests import run_test, SERVICES


@pytest.mark.parametrize("service", SERVICES)
def test_create(service):
    run_test(
        service=service,
        path="create",
        method="POST",
        headers={"Content-Type": "application/xml"},
        status_code=422,
        data=f"""<?xml version="1.0" encoding="UTF-8" ?><service_key>{service}</service_key><data>1</data>""",
    )


@pytest.mark.parametrize("service", SERVICES)
def test_read(service):
    run_test(
        service=service,
        path="read",
        method="GET",
        headers={"Content-Type": "application/xml"},
        status_code=422,
        data=f"""<?xml version="1.0" encoding="UTF-8" ?><service_key>{service}</service_key>""",
    )


@pytest.mark.parametrize("service", SERVICES)
def test_update(service):
    run_test(
        service=service,
        path="update",
        method="PUT",
        headers={"Content-Type": "application/xml"},
        status_code=422,
        data=f"""<?xml version="1.0" encoding="UTF-8" ?><service_key>{service}</service_key><data>2</data>""",
    )


@pytest.mark.parametrize("service", SERVICES)
def test_delete(service):
    run_test(
        service=service,
        path="delete",
        method="DELETE",
        headers={"Content-Type": "application/xml"},
        status_code=422,
        data=f"""<?xml version="1.0" encoding="UTF-8" ?><service_key>{service}</service_key>""",
    )

