from tests.models import BgpNeighbor, BgpPeerType, Interface, Subinterface


SPINE1 = "clab-sr-linux-mclag-spine1"
SPINE2 = "clab-sr-linux-mclag-spine2"


LEAF1 = "clab-sr-linux-mclag-leaf1"
LEAF2 = "clab-sr-linux-mclag-leaf2"
LEAF3 = "clab-sr-linux-mclag-leaf3"


CLIENT1 = "clab-sr-linux-mclag-client1"
CLIENT2 = "clab-sr-linux-mclag-client2"


BGP_NEIGHBORS_DEFINITION = [
    (
        SPINE1,
        [
            BgpNeighbor(
                peer_address="192.0.2.1",
                peer_as=4200000003,
                peer_type=BgpPeerType.EBGP,
                group="underlay_leaf",
            ),
            BgpNeighbor(
                peer_address="192.0.2.3",
                peer_as=4200000004,
                peer_type=BgpPeerType.EBGP,
                group="underlay_leaf",
            ),
            BgpNeighbor(
                peer_address="192.0.2.5",
                peer_as=4200000005,
                peer_type=BgpPeerType.EBGP,
                group="underlay_leaf",
            ),
            BgpNeighbor(
                peer_address="198.51.100.3",
                peer_as=4200000666,
                peer_type=BgpPeerType.IBGP,
                group="overlay_leaf",
            ),
            BgpNeighbor(
                peer_address="198.51.100.4",
                peer_as=4200000666,
                peer_type=BgpPeerType.IBGP,
                group="overlay_leaf",
            ),
            BgpNeighbor(
                peer_address="198.51.100.5",
                peer_as=4200000666,
                peer_type=BgpPeerType.IBGP,
                group="overlay_leaf",
            ),
        ],
    ),
    (
        SPINE2,
        [
            BgpNeighbor(
                peer_address="192.0.2.7",
                peer_as=4200000003,
                peer_type=BgpPeerType.EBGP,
                group="underlay_leaf",
            ),
            BgpNeighbor(
                peer_address="192.0.2.9",
                peer_as=4200000004,
                peer_type=BgpPeerType.EBGP,
                group="underlay_leaf",
            ),
            BgpNeighbor(
                peer_address="192.0.2.11",
                peer_as=4200000005,
                peer_type=BgpPeerType.EBGP,
                group="underlay_leaf",
            ),
            BgpNeighbor(
                peer_address="198.51.100.3",
                peer_as=4200000666,
                peer_type=BgpPeerType.IBGP,
                group="overlay_leaf",
            ),
            BgpNeighbor(
                peer_address="198.51.100.4",
                peer_as=4200000666,
                peer_type=BgpPeerType.IBGP,
                group="overlay_leaf",
            ),
            BgpNeighbor(
                peer_address="198.51.100.5",
                peer_as=4200000666,
                peer_type=BgpPeerType.IBGP,
                group="overlay_leaf",
            ),
        ],
    ),
    (
        LEAF1,
        [
            BgpNeighbor(
                peer_address="192.0.2.0",
                peer_as=4200000001,
                peer_type=BgpPeerType.EBGP,
                group="underlay_spine",
            ),
            BgpNeighbor(
                peer_address="192.0.2.6",
                peer_as=4200000002,
                peer_type=BgpPeerType.EBGP,
                group="underlay_spine",
            ),
            BgpNeighbor(
                peer_address="198.51.100.1",
                peer_as=4200000666,
                peer_type=BgpPeerType.IBGP,
                group="overlay_spine",
            ),
            BgpNeighbor(
                peer_address="198.51.100.2",
                peer_as=4200000666,
                peer_type=BgpPeerType.IBGP,
                group="overlay_spine",
            ),
        ],
    ),
    (
        LEAF2,
        [
            BgpNeighbor(
                peer_address="192.0.2.2",
                peer_as=4200000001,
                peer_type=BgpPeerType.EBGP,
                group="underlay_spine",
            ),
            BgpNeighbor(
                peer_address="192.0.2.8",
                peer_as=4200000002,
                peer_type=BgpPeerType.EBGP,
                group="underlay_spine",
            ),
            BgpNeighbor(
                peer_address="198.51.100.1",
                peer_as=4200000666,
                peer_type=BgpPeerType.IBGP,
                group="overlay_spine",
            ),
            BgpNeighbor(
                peer_address="198.51.100.2",
                peer_as=4200000666,
                peer_type=BgpPeerType.IBGP,
                group="overlay_spine",
            ),
        ],
    ),
    (
        LEAF3,
        [
            BgpNeighbor(
                peer_address="192.0.2.4",
                peer_as=4200000001,
                peer_type=BgpPeerType.EBGP,
                group="underlay_spine",
            ),
            BgpNeighbor(
                peer_address="192.0.2.10",
                peer_as=4200000002,
                peer_type=BgpPeerType.EBGP,
                group="underlay_spine",
            ),
            BgpNeighbor(
                peer_address="198.51.100.1",
                peer_as=4200000666,
                peer_type=BgpPeerType.IBGP,
                group="overlay_spine",
            ),
            BgpNeighbor(
                peer_address="198.51.100.2",
                peer_as=4200000666,
                peer_type=BgpPeerType.IBGP,
                group="overlay_spine",
            ),
        ],
    ),
]


INTERFACES_DEFINITION = [
    (
        SPINE1,
        [
            Interface(name="ethernet-1/1"),
            Subinterface(name="ethernet-1/1", index=0, ip_address="192.0.2.0/31"),
            Interface(name="ethernet-1/2"),
            Subinterface(name="ethernet-1/2", index=0, ip_address="192.0.2.2/31"),
            Interface(name="ethernet-1/3"),
            Subinterface(name="ethernet-1/3", index=0, ip_address="192.0.2.4/31"),
            Interface(name="system0"),
            Subinterface(name="system0", index=0, ip_address="198.51.100.1/32"),
        ],
    ),
    (
        SPINE2,
        [
            Interface(name="ethernet-1/1"),
            Subinterface(name="ethernet-1/1", index=0, ip_address="192.0.2.6/31"),
            Interface(name="ethernet-1/2"),
            Subinterface(name="ethernet-1/2", index=0, ip_address="192.0.2.8/31"),
            Interface(name="ethernet-1/3"),
            Subinterface(name="ethernet-1/3", index=0, ip_address="192.0.2.10/31"),
            Interface(name="system0"),
            Subinterface(name="system0", index=0, ip_address="198.51.100.2/32"),
        ],
    ),
    (
        LEAF1,
        [
            Interface(name="ethernet-1/1"),
            Subinterface(name="ethernet-1/1", index=0, ip_address="192.0.2.1/31"),
            Interface(name="ethernet-1/2"),
            Subinterface(name="ethernet-1/2", index=0, ip_address="192.0.2.7/31"),
            Interface(name="ethernet-1/3"),
            Interface(name="irb1"),
            Subinterface(name="irb1", index=111, ip_address="203.0.113.1/25"),
            Subinterface(name="irb1", index=222, ip_address="203.0.113.129/25"),
            Interface(name="lag1"),
            Interface(name="system0"),
            Subinterface(name="system0", index=0, ip_address="198.51.100.3/32"),
        ],
    ),
    (
        LEAF2,
        [
            Interface(name="ethernet-1/1"),
            Subinterface(name="ethernet-1/1", index=0, ip_address="192.0.2.3/31"),
            Interface(name="ethernet-1/2"),
            Subinterface(name="ethernet-1/2", index=0, ip_address="192.0.2.9/31"),
            Interface(name="ethernet-1/3"),
            Interface(name="irb1"),
            Subinterface(name="irb1", index=111, ip_address="203.0.113.1/25"),
            Subinterface(name="irb1", index=222, ip_address="203.0.113.129/25"),
            Interface(name="lag1"),
            Interface(name="system0"),
            Subinterface(name="system0", index=0, ip_address="198.51.100.4/32"),
        ],
    ),
    (
        LEAF3,
        [
            Interface(name="ethernet-1/1"),
            Subinterface(name="ethernet-1/1", index=0, ip_address="192.0.2.5/31"),
            Interface(name="ethernet-1/2"),
            Subinterface(name="ethernet-1/2", index=0, ip_address="192.0.2.11/31"),
            Interface(name="ethernet-1/3"),
            Interface(name="irb1"),
            Subinterface(name="irb1", index=111, ip_address="203.0.113.1/25"),
            Interface(name="system0"),
            Subinterface(name="system0", index=0, ip_address="198.51.100.5/32"),
        ],
    ),
    (
        CLIENT1,
        [
            Interface(name="ethernet-1/1"),
            Interface(name="ethernet-1/2"),
            Interface(name="lag1"),
            Subinterface(name="lag1", index=111, ip_address="203.0.113.2/25"),
            Subinterface(name="lag1", index=222, ip_address="203.0.113.130/25"),
        ],
    ),
    (
        CLIENT2,
        [
            Interface(name="ethernet-1/1"),
            Subinterface(name="ethernet-1/1", index=111, ip_address="203.0.113.3/25"),
        ],
    ),
]
