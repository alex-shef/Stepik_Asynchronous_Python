import os
import asyncio
import time

import aiofiles
import aiocsv
import json


async def process_csv_file(file_path, semaphore, output_dict):
    async with semaphore:
        async with aiofiles.open(file_path, mode='r') as file:
            reader = aiocsv.AsyncDictReader(file, delimiter=';')
            async for row in reader:
                output_dict[row.get('Состояние авто')] += int(row.get('Стоимость авто'))


async def process_directory(directory, semaphore, output_dict):
    for root, _, files in os.walk(directory):
        tasks = [process_csv_file(os.path.join(root, file), semaphore, output_dict) for file in files]
        await asyncio.gather(*tasks)


async def main():
    output_dict = {'Б/У': 0, 'Новый': 0}
    semaphore = asyncio.Semaphore(1000)  # Ограничение на количество открытых файлов
    directory = '..\For_Asynchronous_Python\Задача 3'  # Путь к основной папке
    await process_directory(directory, semaphore, output_dict)

    # Запись результатов в JSON файл
    async with aiofiles.open('output.json', mode='w', encoding='utf-8') as json_file:
        await json_file.write(json.dumps(output_dict, ensure_ascii=False, indent=4))


# Запускаем асинхронную функцию main()
start_time = time.time()
asyncio.run(main())
end_time = time.time()

execution_time = end_time - start_time
print("Время выполнения скрипта:", execution_time, "секунд")
