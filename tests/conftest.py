import os
from grpc import FutureTimeoutError
import pytest
from pygnmi.client import gNMIclient, gNMIException

from tests.constants import GNMI_PORT


@pytest.fixture(scope="function")
def gnmi_client(device):
    sr_username = os.getenv("SR_USERNAME")
    sr_password = os.getenv("SR_PASSWORD")

    if not sr_username or not sr_password:
        pytest.skip("Credentials are absent, skipping gNMI client tests")
    assert device, "Device hostname was not provided"

    try:
        with gNMIclient(
            target=(device, GNMI_PORT),
            username=sr_username,
            password=sr_password,
            insecure=True,
        ) as client:
            yield client
    except FutureTimeoutError:
        pytest.fail("gNMI client connection timed out")
    except gNMIException as e:
        pytest.fail(f"gNMI client connection failed: {e}")
