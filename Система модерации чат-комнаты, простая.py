import asyncio
from task_1_message import messages

# Список запрещенных слов
banned_words = ['ошибка', 'баг', 'отладка', 'память', 'процессор', 'компиляция', 'алгоритм', 'функция', 'база данных',
                'интерфейс']


async def check_message(message):
    # Проверка сообщения на наличие запрещенных слов
    for message_word in message["message"].lower().split():
        if ''.join(filter(str.isalpha, message_word)) in banned_words:
            # Отмена задачи, если найдено запрещенное слово
            asyncio.current_task().cancel()
            print(f"В сообщении {message['message_id']} стоп-слово: task.done(): False")
            return
    # Если запрещенных слов не найдено, печатаем сообщение
    print(f"{message['message_id']}: {message['message']}")


async def main():
    try:
        tasks = [asyncio.create_task(check_message(message)) for message in messages]
        await asyncio.gather(*tasks)
    except asyncio.CancelledError:
        pass


# Запуск главной асинхронной функции
asyncio.run(main())
