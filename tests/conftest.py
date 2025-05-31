import os
from grpc import FutureTimeoutError
import pytest
from pygnmi.client import gNMIclient, gNMIException

from tests.constants import GNMI_PORT


@pytest.fixture(scope="function")
def gnmi_client(device):
    sr_username = os.getenv("SR_USERNAME")
    sr_password = os.getenv("SR_PASSWORD")
    try:
        with gNMIclient(
            target=(device, GNMI_PORT),
            username=sr_username,
            password=sr_password,
            insecure=True,
        ) as client:
            yield client
    except gNMIException as e:
        pytest.fail(f"gNMI client connection failed: {e}")
    except FutureTimeoutError as e:
        pytest.fail(f"gNMI client connection timed out: {e}")
