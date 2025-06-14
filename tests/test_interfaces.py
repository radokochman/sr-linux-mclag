import pytest

from tests.constants import (
    EXPECTED_INTERFACE_ADMIN_STATE,
    EXPECTED_INTERFACE_OPER_STATE,
)
from tests.helpers import build_path_for_interface, strip_returned_value
from tests.inventory import INTERFACES_DEFINITION
from tests.models import Subinterface


@pytest.mark.parametrize("device,interfaces", INTERFACES_DEFINITION)
def test_interface_admin_state_enabled(gnmi_client, device, interfaces):
    for interface in interfaces:
        path = build_path_for_interface(interface, "admin-state")

        result = gnmi_client.get(path=[path], encoding="json_ietf")
        admin_state = strip_returned_value(result)
        assert admin_state == EXPECTED_INTERFACE_ADMIN_STATE, (
            f"Expected admin-state for interface {interface} to be ",
            f'"{EXPECTED_INTERFACE_ADMIN_STATE}", got "{admin_state}"',
        )


@pytest.mark.parametrize("device,interfaces", INTERFACES_DEFINITION)
def test_interface_oper_state_up(gnmi_client, device, interfaces):
    for interface in interfaces:
        path = build_path_for_interface(interface, "oper-state")

        result = gnmi_client.get(path=[path], encoding="json_ietf")
        oper_state = strip_returned_value(result)
        assert oper_state == EXPECTED_INTERFACE_OPER_STATE, (
            f"Expected oper-state for interface {interface} to be "
            f'"{EXPECTED_INTERFACE_OPER_STATE}", got "{oper_state}"'
        )


@pytest.mark.parametrize("device,interfaces", INTERFACES_DEFINITION)
def test_subinterface_ipv4_address_configured(gnmi_client, device, interfaces):
    for interface in interfaces:
        if not isinstance(interface, Subinterface):
            # Skip interfaces that are not subinterfaces
            continue

        if not interface.ip_address:
            # Skip subinterfaces without IP address
            continue

        path = build_path_for_interface(interface, "ipv4/address")
        result = gnmi_client.get(path=[path], encoding="json_ietf")
        configured_ipv4_address = strip_returned_value(result)["address"][0][
            "ip-prefix"
        ]
        assert configured_ipv4_address == interface.ip_address, (
            f'Expected configured IPv4 address for interface {interface} to be "{interface.ip_address}", '
            f'got "{configured_ipv4_address}"'
        )
