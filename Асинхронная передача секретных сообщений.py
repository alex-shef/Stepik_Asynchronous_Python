import asyncio

codes = ["56FF4D", "A3D2F7", "B1C94E", "F56A1D", "D4E6F1",
         "A1B2C3", "D4E5F6", "A7B8C9", "D0E1F2", "A3B4C5",
         "D6E7F8", "A9B0C1", "D2E3F4", "A5B6C7", "D8E9F0"]

messages = ["Привет, мир!", "Как дела?", "Что нового?", "Добрый день!", "Пока!",
            "Спокойной ночи!", "Удачного дня!", "Всего хорошего!", "До встречи!", "Счастливого пути!",
            "Успехов в работе!", "Приятного аппетита!", "Хорошего настроения!", "Спасибо за помощь!",
            "Всего наилучшего!"]


# Асинхронная функция, которая выводит на экран код
async def print_code(code):
    print(f"Код: {code}")


# Асинхронная функция обратного вызова, которая выводит на экран сообщение
async def print_message(task):
    message = messages[codes.index(task.get_name())]
    print(f"Сообщение: {message}")
    await print_code(task.get_name())


def on_completion(task):
    asyncio.create_task(print_message(task))


# Создание и запуск задачи для асинхронной функции
async def main():
    tasks = []
    for code in codes:
        task = asyncio.create_task(asyncio.sleep(0), name=code)  # Создаем задачу, которая ничего не делает
        task.add_done_callback(on_completion)
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
