import threading
import time
from dataclasses import dataclass
import httpx
from bs4 import BeautifulSoup
from typing import Any


@dataclass
class BaseParser:
    url: str
    page: str
    semaphore: Any = None

    def get_page(self, url):
        with httpx.Client() as client:
            response = client.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                return soup
            else:
                print(f"Failed to retrieve the page. Status code: {response.status_code}")

    def get_page_links(self):
        with httpx.Client() as client:
            response = client.get(f"{self.url}{self.page}")
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

    def get_page_title(self, extracted_url):
        with self.semaphore:

            url = ''.join((self.url, extracted_url))
            soup = self.get_page(url)
            if soup:
                title = soup.select_one('h1.hero-heading').get_text()
                print(title)
            else:
                print("Page not found")

    def get_titles(self, extracted_urls):
        for url in extracted_urls:
            extracted_url = ''.join((self.url, url))
            self.get_page_title(extracted_url)

    def run(self):
        self.semaphore = threading.Semaphore(8)
        extracted_urls = self.get_page_links()
        print(extracted_urls)
        ext_url = (i for i in extracted_urls)
        # Create threads and start them for the get_titles method
        threads = [threading.Thread(target=parser.get_page_title, args=(next(ext_url),)) for _ in range(20)]
        for thread in threads:
            thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()


def start():
    url = "https://jobs.coxenterprises.com/"
    page = "en/jobs/"
    parser = BaseParser(url, page)

    # Create threads and start them
    threads = [threading.Thread(target=parser.run) for _ in range(4)]
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    start_time = time.time()
    url = "https://jobs.coxenterprises.com/"
    page = "en/jobs/"
    parser = BaseParser(url, page)
    parser.run()
    print(f"Execution time: {time.time()-start_time}")
