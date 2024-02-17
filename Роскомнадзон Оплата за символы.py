import asyncio
import time

import aiofiles
import aiofiles.os as aos
from json import dumps


async def read(file):
    async with aiofiles.open(file, encoding='utf-8') as f:
        for line in await f.readlines():
            name, message = line[22:].split(': ')
            data[name] = data.get(name, 0) + len(message) * .03


async def main():
    await asyncio.gather(*(read(i.path) for i in await aos.scandir('chat_log')))

    payment = {k: f'{round(v, 2)}р' for k, v in sorted(data.items(), key=lambda x: -x[1])}
    print(dumps(payment, indent=4, ensure_ascii=False))

data = {}

# Запускаем асинхронную функцию main()
start_time = time.time()
asyncio.run(main())
end_time = time.time()

execution_time = end_time - start_time
print("Время выполнения скрипта:", execution_time, "секунд")
