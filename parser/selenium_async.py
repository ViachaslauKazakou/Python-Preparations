"""
we can Use selenium-async instead base selenium
"""

import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from aiohttp import ClientSession


async def fetch_data(url):
    chrome_service = Service('path/to/chromedriver')  # Укажите путь к вашему драйверу
    driver = webdriver.Chrome(service=chrome_service)
    driver.get(url)

    title = driver.title
    print(f"Page title: {title}")

    driver.quit()


async def main():
    urls = ['https://example.com', 'https://google.com']  # Список URL-адресов для посещения

    tasks = [fetch_data(url) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
