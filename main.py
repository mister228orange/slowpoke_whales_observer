import asyncio
from aiodecorators import Semaphore
from config import Config
from typing import List
from Holder import Holder


SLOWPOKE_ASSET = "EQDK3ReFkb6L3uE3GmMDJaxWby4PA_UYGClgFfJuXY52-TOK"


@Semaphore(Config.MAX_CONCURRENT_TONAPI_REQUESTS)
async def handle_holder(holder, liquid_pair_assets):
    slowpoke_amount = await holder.get_slowpoke_amount()


async def get_holders(asset) -> List[Holder]:
    pass


async def main(asset_addr):
    holders = await get_holders(asset_addr)
    tasks = [
        asyncio.create_task(handle_holder(holders))
    ]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main(SLOWPOKE_ASSET))
