from datetime import datetime
import os
import json
import csv
import asyncio
import time

import aiofiles


async def process_log_file(file_path, output_data):
    async with aiofiles.open(file_path, mode='r', encoding='utf-8') as file:
        log_data = await file.read()
        try:
            log = json.loads(log_data)
            for log_entry in log:
                if log_entry.get('HTTP-статус') == 200:
                    # Преобразование строки в объект datetime с помощью старого формата
                    old_date = datetime.strptime(log_entry.get('Время и дата'), '%Y-%m-%d %H:%M:%S')
                    # Преобразование объекта datetime в строку с новым форматом
                    log_entry['Время и дата'] = old_date.strftime('%d.%m.%Y %H:%M:%S')
                    output_data.append(log_entry)
        except json.JSONDecodeError:
            print(f"Error decoding JSON in file: {file_path}")


async def main():
    output_file_path = 'successful_attempts.csv'
    # Open output CSV file
    async with aiofiles.open(output_file_path, mode='w', encoding='utf-8-sig', newline='') as csvfile:
        fieldnames = ['Время и дата', 'IP-адрес', 'User-Agent', 'Запрошенный URL', 'HTTP-статус', 'Реферер',
                      'Cookie', 'Размер страницы и заголовки ответа', 'Метод запроса', 'Информация об ошибке']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
        # Write CSV headers
        await writer.writeheader()
        # Find log files in the directory
        log_directory = '..\For_Asynchronous_Python\logs'
        # Process each log file asynchronously
        logs = []
        tasks = [process_log_file(os.path.join(log_directory, file), logs) for file in os.listdir(log_directory)]
        await asyncio.gather(*tasks)

        logs.sort(key=lambda x: datetime.strptime(x['Время и дата'], '%d.%m.%Y %H:%M:%S'))

        # Write sorted logs to CSV file
        for log_entry in logs:
            await writer.writerow(log_entry)


# Запускаем асинхронную функцию main()
start_time = time.time()
asyncio.run(main())
end_time = time.time()

execution_time = end_time - start_time
print("Время выполнения скрипта:", execution_time, "секунд")
