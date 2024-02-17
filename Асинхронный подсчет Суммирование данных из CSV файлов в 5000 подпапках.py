import asyncio
import aiofiles
import os
import time


async def read_file(file):
    # читаем файл асинхронно и возвращаем число
    async with aiofiles.open(file, mode="r") as f:
        number = await f.read()
        return int(number)


async def main():
    # Главная директория с подпапками и файлами
    main_directory = "5000folder"
    total_sum = 0

    # Обходим каждую подпапку
    for root, dirs, files in os.walk(main_directory):
        # Создаем список задач для чтения каждого CSV файла в текущей подпапке
        tasks = [asyncio.create_task(read_file(os.path.join(root, file))) for file in files]
        # Ждем, пока все задачи завершатся
        partial_sums = await asyncio.gather(*tasks)
        # Суммируем частичные суммы для каждой подпапки
        total_sum += sum(partial_sums)

    return total_sum

# запускаем асинхронную функцию main
start_time = time.time()
total_sum = asyncio.run(main())
end_time = time.time()
execution_time = end_time - start_time
print("Сумма всех чисел:", total_sum)
print("Время выполнения скрипта:", execution_time, "секунд")
