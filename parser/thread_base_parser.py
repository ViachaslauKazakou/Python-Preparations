import threading
import time
from dataclasses import dataclass
import httpx
from bs4 import BeautifulSoup
from typing import Any
from parser.base_parser import BaseParser
import asyncio
import gc


class ThreadParser(BaseParser):

    semaphore: Any = None

    def get_page(self, url):
        with httpx.Client() as client:
            response = client.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                return soup
            else:
                print(f"Failed to retrieve the page. Status code: {response.status_code}")

    def get_page_title(self, extracted_url):
        with self.semaphore:
            super().get_page_title(extracted_url)

    def process(self):
        super().process()
        self.title = []
        self.semaphore = threading.Semaphore(4)
        ext_url = (''.join((self.site_url, i)) for i in self.extracted_urls)
        threads = [threading.Thread(target=self.get_page_title, args=(next(ext_url),)) for _ in range(len(self.extracted_urls))]
        for thread in threads:
            thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()
        print("- "*40)
        [print(num+1, item) for num, item in enumerate(self.title)]


if __name__ == "__main__":
    start_time = time.time()
    parser = ThreadParser("https://jobs.coxenterprises.com")
    parser.process()
    print(f"Execution time: {time.time()-start_time}")

    print(gc.get_stats())
