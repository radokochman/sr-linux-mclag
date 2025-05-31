from tests.models import Interface, Subinterface


def strip_returned_value(result: dict) -> str:
    return result["notification"][0]["update"][0]["val"]


def build_path_for_interface(interface: Interface | Subinterface, leaf: str) -> str:
    if isinstance(interface, Interface):
        return f"/interface[name={interface.name}]/{leaf}"
    return f"/interface[name={interface.name}]/subinterface[index={interface.index}]/{leaf}"
