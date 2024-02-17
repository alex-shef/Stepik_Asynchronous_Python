import os
import asyncio
import time

import aiofiles
import aiocsv
import json


async def process_csv_file(file_path, semaphore, output_list):
    async with semaphore:
        async with aiofiles.open(file_path, mode='r', encoding='utf-8-sig') as file:
            reader = aiocsv.AsyncReader(file)
            # Читаем заголовки из первой строки
            headers = await reader.__anext__()

            async for row in reader:
                if row[6] == '100':
                    # Создаем словарь из заголовков и значений строки
                    row_dict = {header: value for header, value in zip(headers, row)}
                    output_list.append(row_dict)


async def process_directory(directory, semaphore, output_list):
    for root, _, files in os.walk(directory):
        tasks = [process_csv_file(os.path.join(root, file), semaphore, output_list) for file in files]
        await asyncio.gather(*tasks)


async def main():
    output_list = []
    semaphore = asyncio.Semaphore(1000)  # Ограничение на количество открытых файлов
    directory = '..\For_Asynchronous_Python\Задача Студенты'  # Путь к основной папке
    await process_directory(directory, semaphore, output_list)

    # Сортировка по ключу 'Телефон для связи'
    output_list.sort(key=lambda x: x['Телефон для связи'])

    # Запись результатов в JSON файл
    async with aiofiles.open('output.json', mode='w', encoding='utf-8') as json_file:
        await json_file.write(json.dumps(output_list, ensure_ascii=False, indent=4))


# Запускаем асинхронную функцию main()
start_time = time.time()
asyncio.run(main())
end_time = time.time()

execution_time = end_time - start_time
print("Время выполнения скрипта:", execution_time, "секунд")
