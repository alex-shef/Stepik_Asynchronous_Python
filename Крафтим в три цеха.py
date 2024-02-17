import asyncio

# Каждое значение словаря, это необходимое количество ресурса для изготовления предмета

stone_resources_dict = {
    'Каменная плитка': 10,
    'Каменная ваза': 40,
    'Каменный столб': 50,
}

metal_resources_dict = {
    'Металлическая цепь': 6,
    'Металлическая рамка': 24,
    'Металлическая ручка': 54,
}

cloth_resources_dict = {
    'Тканевая занавеска': 8,
    'Тканевый чехол': 24,
    'Тканевое покрывало': 48,
}

stone_storage = 0
metal_storage = 0
cloth_storage = 0
stone_event = asyncio.Event()
metal_event = asyncio.Event()
cloth_event = asyncio.Event()
stone_condition = asyncio.Condition()
metal_condition = asyncio.Condition()
cloth_condition = asyncio.Condition()


async def gather_stone():
    global stone_storage
    while True:
        await asyncio.sleep(1)
        if stone_event.is_set():  # Проверяем, установлено ли событие
            break  # Если событие установлено, завершаем выполнение корутины
        stone_storage += 10
        print(f"Добыто 10 ед. камня. На складе {stone_storage} ед.")
        async with stone_condition:
            stone_condition.notify()

async def gather_metal():
    global metal_storage
    while True:
        await asyncio.sleep(1)
        if metal_event.is_set():  # Проверяем, установлено ли событие
            break  # Если событие установлено, завершаем выполнение корутины
        metal_storage += 6
        print(f"Добыто 6 ед. металла. На складе {metal_storage} ед.")
        async with metal_condition:
            metal_condition.notify()

async def gather_cloth():
    global cloth_storage
    while True:
        await asyncio.sleep(1)
        if cloth_event.is_set():  # Проверяем, установлено ли событие
            break  # Если событие установлено, завершаем выполнение корутины
        cloth_storage += 8
        print(f"Добыто 8 ед. ткани. На складе {cloth_storage} ед.")
        async with cloth_condition:
            cloth_condition.notify()


async def craft_stone_items():
    global stone_storage
    async with stone_condition:
        for item, cost in stone_resources_dict.items():
            await stone_condition.wait_for(lambda: stone_storage >= cost)
            print(f"Изготовлен {item} из камня.")
            stone_storage -= cost
        else:
            stone_event.set()  # Сигнализируем о завершении производства

async def craft_metal_items():
    global metal_storage
    async with metal_condition:
        for item, cost in metal_resources_dict.items():
            await metal_condition.wait_for(lambda: metal_storage >= cost)
            print(f"Изготовлен {item} из металла.")
            metal_storage -= cost
        else:
            metal_event.set()  # Сигнализируем о завершении производства

async def craft_cloth_items():
    global cloth_storage
    async with cloth_condition:
        for item, cost in cloth_resources_dict.items():
            await cloth_condition.wait_for(lambda: cloth_storage >= cost)
            print(f"Изготовлен {item} из ткани.")
            cloth_storage -= cost
        else:
            cloth_event.set()  # Сигнализируем о завершении производства


async def main():
    gather_stone_task = asyncio.create_task(gather_stone())
    gather_metal_task = asyncio.create_task(gather_metal())
    gather_cloth_task = asyncio.create_task(gather_cloth())
    craft_stone_task = asyncio.create_task(craft_stone_items())
    craft_metal_task = asyncio.create_task(craft_metal_items())
    craft_cloth_task = asyncio.create_task(craft_cloth_items())
    await asyncio.gather(gather_stone_task, gather_metal_task, gather_cloth_task,
                         craft_stone_task, craft_metal_task, craft_cloth_task)


if __name__ == "__main__":
    asyncio.run(main())
