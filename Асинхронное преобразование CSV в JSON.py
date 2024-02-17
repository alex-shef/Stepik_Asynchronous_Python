import asyncio

import aiocsv
import aiofiles
import json
import time

from aiofiles import open as aio_open


async def read_csv_and_write_json(input_file, output_file):
    async with aiofiles.open(input_file, mode='r', encoding='utf-8-sig') as file:
        # Создаем асинхронный читатель CSV файла с указанием правильного разделителя
        reader = aiocsv.AsyncReader(file, delimiter=';')

        # Читаем заголовки из первой строки
        headers = await reader.__anext__()

        data = []
        async for row in reader:
            # Создаем словарь из заголовков и значений строки
            row_dict = {header: value for header, value in zip(headers, row)}
            data.append(row_dict)

    # Записываем данные в JSON файл
    async with aiofiles.open(output_file, mode='w', encoding='utf-8') as json_file:
        await json_file.write(json.dumps(data, ensure_ascii=False, indent=4))


async def main():
    await read_csv_and_write_json('adress_1000000.csv', 'adress_1000000.json')


# Запускаем асинхронную функцию main()
start_time = time.time()
asyncio.run(main())
end_time = time.time()

execution_time = end_time - start_time
print("Время выполнения скрипта:", execution_time, "секунд")
