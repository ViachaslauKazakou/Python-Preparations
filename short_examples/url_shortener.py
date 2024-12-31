import hashlib
import threading

class URLShortener:
    def __init__(self):
        self.shortener = {}
        self.lock = threading.Lock()

    def shorten(self, long_url):
        with self.lock:
            if long_url in self.shortener.values():
                print("URL already shortened")
                return list(self.shortener.keys())[list(self.shortener.values()).index(long_url)]

            hash_object = hashlib.md5(long_url.encode())
            short_url = hash_object.hexdigest()[:6]
            
            self.shortener[short_url] = long_url

            return short_url

    def redirect(self, short_url):
        with self.lock:
            return self.shortener.get(short_url, "URL not found")
        


if __name__ == "__main__":
    shortener = URLShortener()
    
    # Example usage
    long_url = "https://www.google.com"
    short_url = shortener.shorten(long_url)
    print(f"Short URL for {long_url}: {short_url}")
    print(f"Redirecting {short_url}: {shortener.redirect(short_url)}")
    
    # Test concurrency
    def shorten_and_print(url):
        short_url = shortener.shorten(url)
        print(f"Short URL for {url}: {short_url}")

    urls = [
        "https://www.example.com",
        "https://www.example1.com",
        "https://www.example2.com",
        "https://www.example3.com",
        "https://www.example4.com",
        "https://www.example5.com",
        "https://www.example6.com",
        "https://www.example7.com",
        "https://www.example8.com",
        "https://www.example8.com",
        "https://www.example9.com",
        "https://www.example10.com",
        "https://www.example11.com",

    ]

    threads = []
    for url in urls:
        thread = threading.Thread(target=shorten_and_print, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Final shortener dictionary:", shortener.shortener)
    
    import concurrent.futures

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(shortener.redirect, url) for url in shortener.shortener.keys()]
        for future in concurrent.futures.as_completed(futures):
            print(f"Redirecting result: {future.result()}")
            
    for url in shortener.shortener.keys():
        thread = threading.Thread(target=lambda u: print(f"Redirecting {u}: {shortener.redirect(u)}"), args=(url,))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
        
    