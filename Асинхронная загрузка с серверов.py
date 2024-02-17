import asyncio
import random

server_names = {
    "1": "Server_Alpha", "2": "Server_Beta", "3": "Server_Gamma",
    "4": "Server_Delta", "5": "Server_Epsilon"
}

async def load_data(server):
    print(f"Загрузка данных с сервера {server_names[server]} началась")
    await asyncio.sleep(random.randint(0, 5))  # Имитация загрузки данных
    print(f"Загрузка данных с сервера {server_names[server]} завершена")

async def main(n):
    tasks = [load_data(str(i)) for i in range(1, n+1)]
    await asyncio.gather(*tasks)

asyncio.run(main(5))
