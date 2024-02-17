import asyncio


async def database_access(user):
    print(f"Пользователь {user} ожидает доступа к базе данных")
    async with access_control:
        await access_control.wait()  # Ожидание разблокировки доступа
        print(f"Пользователь {user} подключился к БД")
        await asyncio.sleep(1)  # Моделируем работу с базой данных
        print(f"Пользователь {user} отключается от БД")
        access_control.notify()


async def database_controller():
    await asyncio.sleep(2)
    async with access_control:
        access_control.notify()  # Разблокировка одного из ожидающих пользователей


users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eva', 'Frank', 'George', 'Helen', 'Ivan', 'Julia']
access_control = asyncio.Condition()


async def main():
    controller_task = asyncio.create_task(database_controller())
    tasks = [database_access(user) for user in users]
    await asyncio.gather(*tasks)
    await controller_task  # Дожидаемся завершения контроллера


if __name__ == "__main__":
    asyncio.run(main())
