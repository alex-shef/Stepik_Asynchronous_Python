import asyncio
import aiofiles
from aiofiles import os as aos
import time


async def read_file(file):
    # читаем файл асинхронно и возвращаем число
    async with aiofiles.open(file, mode="r") as f:
        number = await f.read()
        return int(number)


async def main():
    # получаем список файлов в папке data
    files = await aos.listdir("5000csv")
    # создаем список задач для каждого файла
    tasks = [asyncio.create_task(read_file("5000csv/" + file)) for file in files]
    # ждем, пока все задачи завершатся
    total_sum = sum(await asyncio.gather(*tasks))
    return total_sum

# запускаем асинхронную функцию main
start_time = time.time()
total_sum = asyncio.run(main())
end_time = time.time()
execution_time = end_time - start_time
print("Сумма всех чисел:", total_sum)
print("Время выполнения скрипта:", execution_time, "секунд")
