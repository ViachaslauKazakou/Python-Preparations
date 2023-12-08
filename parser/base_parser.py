import time
from abc import ABC, abstractmethod
from dataclasses import dataclass

import httpx
import structlog
from bs4 import BeautifulSoup
from typing import Any

log = structlog.get_logger("Parser")


class Parser(ABC):
    @abstractmethod
    async def process(self):
        """
        Base, parse method
        :return:
        """


@dataclass
class BaseParser(Parser):
    site_url: str
    title: list = None
    extracted_urls = []

    def _get_page(self, page_url: str) -> Any:
        with httpx.Client() as client:
            response = client.get(page_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                return soup
            else:
                print(f"Failed to retrieve the page {page_url}. Status code: {response.status_code}")

    def get_page_links(self, page_url):
        if soup := self._get_page(page_url):
            anchor_tags = soup.select("a.stretched-link")
            if anchor_tags:
                for item in anchor_tags:
                    self.extracted_urls.append(item.get("href"))
            else:
                print("No anchor tag found on the page.")
            return

    def get_page_title(self, extracted_url) -> None:
        if soup := self._get_page(extracted_url):
            if soup:
                location = soup.select_one(".job-summary-location>div>ul>li").get_text()
                title = soup.select_one("h1.hero-heading").get_text()
                self.title.append(f"{title}. Location:[ {location} ]")
                # return f"{title}. Location:[ {location} ]"
            else:
                print("Page not found")

    def collect_links(self) -> None:
        print(self.site_url)
        for page in range(2, 6):
            current_url = "".join((self.site_url, f"/en/jobs/?page={page}"))
            print(current_url)
            print("---")
            self.get_page_links(current_url)
        # self.extracted_urls = list(set(self.extracted_urls))
        [print(key + 1, f"{self.site_url}{item}") for key, item in enumerate(self.extracted_urls)]

    def process(self) -> None:
        """
        Parse pipeline without async methods
        :return:
        """
        self.collect_links()


if __name__ == "__main__":
    start_time = time.time()
    url = "https://jobs.coxenterprises.com"
    parser = BaseParser(url)
    parser.process()
    print(f"Execution time: {time.time()-start_time}")
