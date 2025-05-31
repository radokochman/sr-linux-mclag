from dataclasses import dataclass
from enum import Enum


@dataclass
class InterfaceBase:
    name: str


@dataclass
class Subinterface(InterfaceBase):
    index: int
    ip_address: str = None

    def __str__(self):
        return f"{self.name}.{self.index}"


@dataclass
class Interface(InterfaceBase):
    def __str__(self):
        return self.name


class BgpPeerType(Enum):
    EBGP = "ebgp"
    IBGP = "ibgp"


@dataclass
class BgpNeighbor:
    peer_address: str
    peer_as: int
    peer_type: BgpPeerType
    group: str
