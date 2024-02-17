import aiohttp
from bs4 import BeautifulSoup
import asyncio

code_dict = {
    0: 'F',
    1: 'B',
    2: 'D',
    3: 'J',
    4: 'E',
    5: 'C',
    6: 'H',
    7: 'G',
    8: 'A',
    9: 'I'
}


async def fetch_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url = 'https://asyncio.ru/zadachi/1/index.html'  # Замените на нужный URL
    page_content = await fetch_page(url)
    soup = BeautifulSoup(page_content, 'html.parser')
    p_text = soup.find('p').text.strip()
    decrypted_text = ''.join(code_dict[int(char)] for char in p_text)
    print(decrypted_text)  # Вывод расшифрованного текста


if __name__ == '__main__':
    asyncio.run(main())
