from dataclasses import dataclass


@dataclass
class Jetton:
    asset_addr: str
    asset_name: str
    amount: int
