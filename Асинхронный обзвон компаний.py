import asyncio
import companies


async def call_company(company):
    try:
        await asyncio.sleep(company['call_time'])
        if company['call_time'] > 5:
            raise asyncio.CancelledError()
        else:
            print(f"Company {company['Name']}: {company['Phone']} дозвон успешен")
    except asyncio.CancelledError:
        pass


async def main():
    tasks = [asyncio.create_task(call_company(company)) for company in companies.data]
    await asyncio.sleep(10)
    for task in tasks:
        if not task.done():
            task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
