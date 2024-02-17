import aiohttp
import asyncio
from bs4 import BeautifulSoup

TARGET_URL = "https://asyncio.ru/zadachi/4/"  # Замените на вашу целевую страницу
MAX_CONCURRENT_REQUESTS = 5  # Максимальное количество одновременных запросов


async def fetch_html(url, session):
    async with session.get(url) as response:
        return await response.text()


async def extract_image_urls(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    main_tag = soup.find('main')
    img_tags = main_tag.find_all('img')
    return [TARGET_URL + img['src'] for img in img_tags]


async def get_image_size(url, session, semaphore):
    async with semaphore:
        async with session.head(url) as response:
            return int(response.headers.get("Content-Length", 0))


async def main():
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
    async with aiohttp.ClientSession() as session:
        # Скачиваем HTML-контент целевой страницы
        html_content = await fetch_html(TARGET_URL + 'index.html', session)

        # Извлекаем URL-адреса изображений из HTML-контента
        image_urls = await extract_image_urls(html_content)

        # Получаем размер каждого изображения
        tasks = [get_image_size(url, session, semaphore) for url in image_urls]
        sizes = await asyncio.gather(*tasks)

        # Подсчитываем общий размер всех изображений
        total_size = sum(sizes)
        print("Total size of images:", total_size, "bytes")


if __name__ == "__main__":
    asyncio.run(main())
