import asyncio
import time

import aiohttp
from aiohttp import ClientSession
from bs4 import BeautifulSoup

BASE_URL = "https://asyncio.ru/zadachi/3/"
MAX_CONCURRENT_REQUESTS = 5


async def fetch_html(url, session):
    async with session.get(url) as response:
        return await response.text()


async def extract_number(html):
    soup = BeautifulSoup(html, 'html.parser')
    number_tag = soup.find('p', {'id': 'number'})
    if number_tag:
        return int(number_tag.text.strip())
    else:
        return 0


async def process_page(url, session):
    html = await fetch_html(url, session)
    number = await extract_number(html)
    print(f"Processed page {url}, number: {number}")
    return number


async def process_depth1_page(url, session, semaphore):
    async with semaphore:
        html = await fetch_html(url, session)

        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a', {'class': 'link'})

        tasks = []
        for link in links:
            subpage_url = BASE_URL + 'depth1/' + link['href']
            tasks.append(process_page(subpage_url, session))

        results = await asyncio.gather(*tasks)
        print('process_depth1_page results: ', results)

        return results


async def process_main_page(session, semaphore):
    async with semaphore:
        html = await fetch_html(BASE_URL + "index.html", session)

        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a', {'class': 'link'})

        subpage_numbers = []

        tasks = []
        for link in links:
            depth1_url = BASE_URL + link['href']
            tasks.append(process_depth1_page(depth1_url, session, semaphore))

        results = await asyncio.gather(*tasks)
        print('process_main_page results: ', results)

        for sublist in results:
            subpage_numbers.extend(sublist)

        return subpage_numbers


async def main():
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
    async with ClientSession() as session:
        all_numbers = await process_main_page(session, semaphore)
        print("Total sum of numbers on all pages:", sum(all_numbers))


# запускаем асинхронную функцию main
start_time = time.time()
total_sum = asyncio.run(main())
end_time = time.time()
execution_time = end_time - start_time

print("Время выполнения скрипта:", execution_time, "секунд")
