from dataclasses import dataclass
import httpx
import asyncio
from bs4 import BeautifulSoup
from decorators.main import timer
import time
from typing import Any


@dataclass
class BaseParser:
    url: str
    page: str
    semaphore: Any = None
    title: list = None

    async def get_page(self, url):
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                return soup
            else:
                print(f"Failed to retrieve the page {url}. Status code: {response.status_code}")

    async def get_page_links(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.url}{self.page}")
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                anchor_tags = soup.select('a.stretched-link')
                extracted_urls = []
                if anchor_tags:
                    for item in anchor_tags:
                        extracted_urls.append(item.get('href'))
                    print(f"Found {len(extracted_urls)} links")
                    return extracted_urls
                else:
                    print("No anchor tag found on the page.")
            else:
                print(f"Failed to retrieve the page. Status code: {response.status_code}")

    async def get_page_title(self, extracted_url):
        async with self.semaphore:
            if soup := await self.get_page(extracted_url):
                title = soup.select_one('h1.hero-heading').get_text()
                self.title.append(title.strip())
            else :
                print("page_not found")

    async def get_titles(self, extracted_urls):
        for url in extracted_urls:
            extracted_url = ''.join((self.url, url))
            await self.get_page_title(extracted_url)

    async def run(self):
        self.title = []
        self.semaphore = asyncio.Semaphore(8)
        extracted_urls = await self.get_page_links()
        [print(f"{self.url}{item}") for item in extracted_urls]

        # Create a list of coroutine tasks for get_page_title
        tasks = [self.get_page_title(''.join((self.url, url))) for url in extracted_urls]

        # Run the tasks concurrently using asyncio.gather
        await asyncio.gather(*tasks)
        [print(item) for item in self.title]


async def start():
    url = "https://jobs.coxenterprises.com/"
    page = "en/jobs/"
    parser = BaseParser(url, page)
    result = await parser.run()


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(start())
    print(f"Execution time: {time.time()-start_time}")
