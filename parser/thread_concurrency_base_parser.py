import concurrent.futures
import time
from dataclasses import dataclass
from typing import Any, List

import httpx
from bs4 import BeautifulSoup


@dataclass
class BaseParser:
    url: str
    page: str
    semaphore: Any = None
    result: List = None

    def get_page(self, link):
        with httpx.Client() as client:
            response = client.get(link)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                return soup
            else:
                print(f"Failed to retrieve the page. Status code: {response.status_code}")

    def get_page_links(self):
        with httpx.Client() as client:
            response = client.get(f"{self.url}{self.page}")
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                anchor_tags = soup.select("a.stretched-link")
                extracted_urls = []
                if anchor_tags:
                    for item in anchor_tags:
                        extracted_urls.append(item.get("href"))
                    return extracted_urls
                else:
                    print("No anchor tag found on the page.")
            else:
                print(f"Failed to retrieve the main page. Status code: {response.status_code}")

    def get_page_title(self, link):
        uri = "".join((self.url, link))
        soup = self.get_page(uri)
        if soup:
            location = soup.select_one(".job-summary-location>div>ul>li").get_text()
            title = soup.select_one("h1.hero-heading").get_text()
            return f"{title}. Location:[ {location} ]"
        else:
            print("Page not found")

    def run(self):
        self.result = list()
        extracted_urls = self.get_page_links()
        [print(key + 1, f"{self.url}{item}") for key, item in enumerate(extracted_urls)]
        print(f"Found {len(extracted_urls)} links")
        with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
            links = {executor.submit(self.get_page_title, link): link for link in extracted_urls}
            for future in concurrent.futures.as_completed(links):
                page_title = future.result()
                self.result.append(page_title)
        print("------------ Parser finished ----------------")
        print(f"Parsed {len(self.result)} titles\r\n")
        [print(key + 1, f" - {item}") for key, item in enumerate(self.result)]


if __name__ == "__main__":
    start_time = time.time()
    url = "https://jobs.coxenterprises.com"
    page = "/en/jobs/"
    parser = BaseParser(url, page)
    parser.run()
    print(f"\r\nExecution time: {time.time()-start_time}")
