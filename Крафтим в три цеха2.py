import asyncio

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

storage = {
    'stone': 0,
    'metal': 0,
    'cloth': 0
}

events = {
    'stone': asyncio.Event(),
    'metal': asyncio.Event(),
    'cloth': asyncio.Event()
}

conditions = {
    'stone': asyncio.Condition(),
    'metal': asyncio.Condition(),
    'cloth': asyncio.Condition()
}


async def gather_resources(resource_name, resources_dict):
    global storage
    while True:
        await asyncio.sleep(1)
        if events[resource_name].is_set():
            break
        storage[resource_name] += resources_dict[list(resources_dict.keys())[0]]
        print(f"Добыто {resources_dict[list(resources_dict.keys())[0]]} ед. {resource_name}. "
              f"На складе {storage[resource_name]} ед.")
        async with conditions[resource_name]:
            conditions[resource_name].notify()


async def craft_items(resource_name, resources_dict):
    global storage
    async with conditions[resource_name]:
        for item, cost in resources_dict.items():
            await conditions[resource_name].wait_for(
                lambda: storage[resource_name] >= cost)
            print(f"Изготовлен {item} из {resource_name}.")
            storage[resource_name] -= cost
        else:
            events[resource_name].set()


async def main():
    tasks = []
    for resource_name, resources_dict in zip(['stone', 'metal', 'cloth'],
                                             [stone_resources_dict, metal_resources_dict, cloth_resources_dict]):
        tasks.append(asyncio.create_task(gather_resources(resource_name, resources_dict)))
        tasks.append(asyncio.create_task(craft_items(resource_name, resources_dict)))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
