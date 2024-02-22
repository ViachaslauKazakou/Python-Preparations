import asyncio
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, List

import httpx
import structlog
from bs4 import BeautifulSoup

log = structlog.get_logger("Parser")


class Parser(ABC):
    @abstractmethod
    async def process(self) -> None:
        """
        Base, parse method
        :return:
        """


@dataclass
class BaseParser(Parser):
    site_url: str
    title: list = field(default_factory=list)
    extracted_urls: List[str] = field(default_factory=list)

    async def _get_page(self, page_url: str) -> Any:
        async with httpx.AsyncClient() as client:
            response = await client.get(page_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                return soup
            else:
                print(f"Failed to retrieve the page {page_url}. Status code: {response.status_code}")

    async def get_page_links(self, page_url: str) -> None:
        if soup := await self._get_page(page_url):
            anchor_tags = soup.select("a.stretched-link")
            if anchor_tags:
                for item in anchor_tags:
                    self.extracted_urls.append(item.get("href"))
            else:
                print("No anchor tag found on the page.")

    async def get_page_title(self, extracted_url: str) -> Any:
        if soup := await self._get_page(extracted_url):
            if soup:
                location = soup.select_one(".job-summary-location>div>ul>li").get_text()
                title = soup.select_one("h1.hero-heading").get_text()
                return f"{title}. Location:[ {location} ]"
            else:
                print("Page not found")

    async def collect_links(self) -> None:
        print(self.site_url)
        for page in range(2, 6):
            current_url = "".join((self.site_url, f"/en/jobs/?page={page}"))
            print(current_url)
            print("---")
            await self.get_page_links(current_url)
        # self.extracted_urls = list(set(self.extracted_urls))
        [print(key + 1, f"{self.site_url}{item}") for key, item in enumerate(self.extracted_urls)]

    async def process(self) -> None:
        """
        Parse pipeline without async methods
        :return:
        """
        await self.collect_links()


if __name__ == "__main__":
    start_time = time.time()
    url = "https://jobs.coxenterprises.com"
    parser = BaseParser(url)
    asyncio.run(parser.process())
    print(f"Execution time: {time.time()-start_time}")
