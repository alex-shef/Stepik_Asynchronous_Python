import asyncio

wood_resources_dict = {
    'Деревянный меч': 6,
    'Деревянный щит': 12,
    'Деревянный стул': 24,
}

storage = 0
event = asyncio.Event()
condition = asyncio.Condition()


async def gather_wood():
    global storage
    while True:
        await asyncio.sleep(1)
        if event.is_set():  # Проверяем, установлено ли событие
            break  # Если событие установлено, завершаем выполнение корутины
        storage += 2
        print(f"Добыто 2 ед. дерева. На складе {storage} ед.")
        async with condition:
            condition.notify()  # Сообщаем мастерской о появлении новой древесины


async def craft_item():
    global storage
    async with condition:
        for item, cost in wood_resources_dict.items():
            await condition.wait_for(lambda: storage >= cost)
            print(f"Изготовлен {item}.")
            storage -= cost
        else:
            event.set()  # Сигнализируем о завершении производства


async def main():
    gather_wood_task = asyncio.create_task(gather_wood())
    craft_item_task = asyncio.create_task(craft_item())
    await asyncio.gather(gather_wood_task, craft_item_task)


if __name__ == "__main__":
    asyncio.run(main())
