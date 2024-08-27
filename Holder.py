from typing import Set
from Jetton import Jetton


class Holder:
    telegram_id: int
    telegram_username: str
    TON_wallet: str
    Balance: Set[Jetton]

    def __init__(self):
        pass


    async def calc_asset(self, asset_name=None, asset_address=None):
        amount = 0
        if asset_name:
            # calc by name
            self.balance.add(Jetton(asset_name, asset_address, amount))
        elif asset_address:

            pass
        else:
            # calc ton
            self.balance.add(Jetton("TON", "DUbai street house Abay", amount))
