import pytest

from tests.constants import EXPECTED_BGP_PEER_STATE
from tests.helpers import strip_returned_value
from tests.inventory import BGP_NEIGHBORS_DEFINITION


@pytest.mark.parametrize("device,bgp_neighbors", BGP_NEIGHBORS_DEFINITION)
def test_bgp_neighbor_state(gnmi_client, device, bgp_neighbors):
    for neighbor in bgp_neighbors:
        path = f"/network-instance[name=default]/protocols/bgp/neighbor[peer-address={neighbor.peer_address}]"

        result = gnmi_client.get(path=[path], encoding="json_ietf")
        neighbor_data = strip_returned_value(result)

        assert neighbor_data["peer-as"] == neighbor.peer_as, (
            f'Expected BGP neighbor peer AS to be "{neighbor.peer_as}", got "{neighbor_data["peer-as"]}"'
        )
        assert neighbor_data["peer-type"] == neighbor.peer_type.value, (
            f'Expected BGP neighbor peer type to be "{neighbor.peer_type.value}", got ',
            f'"{neighbor_data["peer-type"]}"',
        )
        assert neighbor_data["peer-group"] == neighbor.group, (
            f'Expected BGP neighbor group to be "{neighbor.group}", got "{neighbor_data["group"]}"'
        )
        assert neighbor_data["session-state"] == EXPECTED_BGP_PEER_STATE, (
            f"Expected BGP neighbor session state to be {EXPECTED_BGP_PEER_STATE}, got ",
            f'"{neighbor_data["session-state"]}"',
        )
