import time

import aiohttp
import asyncio

# Список для хранения статус кодов
status_codes = []


async def fetch_page(session, page_number,sem):
    url = f"https://asyncio.ru/zadachi/5/{page_number}.html"
    async with sem:
        async with session.get(url) as response:
            status_code = response.status
            # Добавляем статус код в список
            status_codes.append(int(status_code))
            print(f"Страница {page_number} загружена с кодом статуса: {status_code}")


async def main():
    sem = asyncio.Semaphore(20)
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, 1001):  # Обход страниц от 1 до 999
            task = asyncio.ensure_future(fetch_page(session, i, sem))
            tasks.append(task)

        await asyncio.gather(*tasks)

print(sum(status_codes))


# Запускаем асинхронную функцию main()
start_time = time.time()
asyncio.run(main())
end_time = time.time()

execution_time = end_time - start_time
print("Время выполнения скрипта:", execution_time, "секунд")
