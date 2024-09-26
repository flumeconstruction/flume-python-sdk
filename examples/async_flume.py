from flume import AsyncFlume
import asyncio

flume = AsyncFlume()


async def get_customer_from_item():
    item = await flume.item.retrieve("aa090f33-1432-40cf-9b0c-ca5df2948489")
    customer = await flume.customer.retrieve(item.customer_id)
    return customer


async def main():
    customer = await get_customer_from_item()
    print(customer)

asyncio.run(main())
