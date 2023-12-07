import httpx
import asyncio
from bs4 import BeautifulSoup
from decorators.main import timer
import time
from typing import Any
from base_parser import BaseParser
import gc


class AsyncParser(BaseParser):
    url: str
    page: str
    semaphore = None
    title: list = None

    async def get_page_title(self, extracted_url):
        async with self.semaphore:
            if soup := await self._get_page(extracted_url):
                location = soup.select_one(".job-summary-location>div>ul>li").get_text()
                title = soup.select_one('h1.hero-heading').get_text()
                self.title.append(f"{title}. Location:[ {location} ]")
                return f"{title}. Location:[ {location} ]"
            else:
                print("page_not found")

    async def __get_titles(self, extracted_urls):
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

    async def process(self):
        await super().process()
        self.title = []
        self.semaphore = asyncio.Semaphore(16)
        tasks = [self.get_page_title(''.join((self.site_url, url))) for url in self.extracted_urls]
        await asyncio.gather(*tasks)
        [print(item) for item in self.title]



if __name__ == "__main__":
    start_time = time.time()
    parser = AsyncParser("https://jobs.coxenterprises.com")
    asyncio.run(parser.process())
    print(f"Execution time: {time.time()-start_time}")

    print(gc.get_stats())
    gc.collect(0)
    print(gc.get_stats())
    gc.collect(1)
    print(gc.get_stats())