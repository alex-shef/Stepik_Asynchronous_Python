import asyncio
import aiohttp
from bs4 import BeautifulSoup


async def fetch_data(session, semaphore, base_url, page_name):
    async with semaphore:
        url = f"{base_url}/{page_name}.html"

        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            print(url)
            p_tag = soup.find('p', id='number')
            print(p_tag)
            number = int(p_tag.text.strip())
            return number


async def main():
    base_url = "https://asyncio.ru/zadachi/2/html"
    semaphore = asyncio.Semaphore(5)

    async with aiohttp.ClientSession() as session:
        with open("problem_pages.txt", "r") as file:
            page_names = [line.strip() for line in file.readlines()]

        tasks = [fetch_data(session, semaphore, base_url, page_name) for page_name in page_names]
        results = await asyncio.gather(*tasks)

        total_sum = sum(results)

    return total_sum


result = asyncio.run(main())
print(result)
