import asyncio
from task_2_message import messages

# Список запрещенных слов
banned_words = ["bug", "error", "exception", "fail", "crash", "hang", "slow", "memory leak", "infinite loop",
                "deadlock"]


async def check_message(message):
    # Проверка сообщения на наличие запрещенных слов
    if message['role'] == 'admin':
        print(f"{message['role']}: {message['message']}")
    elif message['role'] == 'moderator':
        for word in banned_words:
            message["message"] = message["message"].replace(word, "****")
        print(f"{message['role']}: {message['message']}")
    elif message['role'] == 'student':
        for word in banned_words:
            if word in message['message']:
                print(f"{message['role']}: В сообщении есть запрещённое слово, сообщение скрыто")
                break
        else:
            print(f"{message['role']}: {message['message']}")
    elif message['role'] == 'black_list_user':
        print(f"{message['role']}: Пользователь забанен, сообщение скрыто")
    else:
        print(f"None: ERROR_USER_NONE")


async def main():
    tasks = [asyncio.create_task(check_message(message), name=message['role']) for message in messages]
    await asyncio.gather(*tasks)


# Запуск главной асинхронной функции
asyncio.run(main())
