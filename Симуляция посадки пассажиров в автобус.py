import asyncio
from bus_passengers import passengers


# Асинхронная функция посадки пассажиров
async def board_passenger(passenger):
    name = passenger["Name"]
    speed = passenger["Speed"]
    job = passenger["Job"]

    try:
        # Ожидание времени, равного скорости посадки пассажира
        await asyncio.sleep(speed)
        # Пассажир успел сесть в автобус
        print(f"{name} сел в автобус.")
    except asyncio.CancelledError:
        # Пассажир не успел сесть в автобус за отведенное время
        print(f"{name} {job} не успел/а вовремя сесть в автобус.")


# Главная асинхронная функция
async def main():
    # Создание задач для каждого пассажира
    tasks = [board_passenger(passenger) for passenger in passengers]

    try:
        # Ожидание завершения всех задач в течение 5 секунд
        await asyncio.wait_for(asyncio.gather(*tasks), timeout=5)
    except asyncio.TimeoutError:
        pass


# Запуск основной асинхронной функции
asyncio.run(main())
