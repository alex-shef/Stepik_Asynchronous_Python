import asyncio
import random


async def scan_port(address, port):
    await asyncio.sleep(1)
    if random.randint(0, 100) == 1:
        print(f"Port {port} on {address} is open")
        return port


async def scan_range(address, start_port, end_port):
    print(f"Scanning ports {start_port}-{end_port} on {address}")
    tasks = [scan_port(address, port) for port in range(start_port, end_port + 1)]
    open_ports = await asyncio.gather(*tasks)
    open_ports = [port for port in open_ports if port is not None]  # Фильтрация None значений (не открытых портов)
    return address, open_ports


async def main(dct):
    results = await asyncio.gather(*(scan_range(address, *ports) for address, ports in dct.items()))
    for result in results:
        if result[1]:
            print(f"Всего найдено открытых портов {len(result[1])} {result[1]} для ip: {result[0]}")


ip_dct = {'192.168.0.1': [0, 100], '192.168.0.2': [225, 300], '192.168.2.5': [150, 185]}
asyncio.run(main(ip_dct))
