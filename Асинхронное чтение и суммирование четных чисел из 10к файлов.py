import asyncio
import aiofiles
from aiofiles import os as aos
import time


async def read_file(file):
    # читаем файл асинхронно и возвращаем число
    async with aiofiles.open(file, mode="r") as f:
        number = await f.read()
        return int(number)


async def process_file(file, semaphore):
    # обрабатываем файл с помощью семафора, чтобы избежать ошибки слишком многих открытых файлов
    async with semaphore:
        number = await read_file(file)
        # если число четное, добавляем его к общей сумме
        if number % 2 == 0:
            global total
            total += number


async def main():
    # создаем семафор с ограничением в 1000 одновременных операций
    semaphore = asyncio.Semaphore(1000)
    # получаем список файлов в папке data
    files = await aos.listdir("files")
    # создаем список задач для каждого файла
    tasks = [asyncio.create_task(process_file("files/" + file, semaphore)) for file in files]
    # ждем, пока все задачи завершатся
    await asyncio.gather(*tasks)
    # выводим результат
    print(total)


# инициализируем переменную для хранения суммы
total = 0
# запускаем асинхронную функцию main
start_time = time.time()
asyncio.run(main())
end_time = time.time()

execution_time = end_time - start_time
print("Время выполнения скрипта:", execution_time, "секунд")
