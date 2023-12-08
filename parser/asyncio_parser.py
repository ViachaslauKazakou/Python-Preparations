import asyncio
import gc
import time

from base_async_parser import BaseParser
from typing import List, Any


class AsyncParser(BaseParser): # type: ignore
    url: str
    page: str
    semaphore = None
    title: List[Any] = []

    async def get_page_title(self, extracted_url: list):
        async with self.semaphore:
            if soup := await self._get_page(extracted_url):
                location = soup.select_one(".job-summary-location>div>ul>li").get_text()
                title = soup.select_one("h1.hero-heading").get_text()
                self.title.append(f"{title}. Location:[ {location} ]")
                return f"{title}. Location:[ {location} ]"
            else:
                print("page_not found")

    async def process(self):
        await super().process()
        self.title = []
        self.semaphore = asyncio.Semaphore(16)
        tasks = [self.get_page_title("".join((self.site_url, url))) for url in self.extracted_urls]
        await asyncio.gather(*tasks)
        [print(item) for item in self.title]


if __name__ == "__main__":
    start_time = time.time()
    parser = AsyncParser("https://jobs.coxenterprises.com")
    asyncio.run(parser.process())
    print(f"Execution time: {time.time()-start_time}")

    print(gc.get_stats())
