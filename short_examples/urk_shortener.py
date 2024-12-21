# Create class to shorten URLs. Get the shortened URL and redirect to the original URL. shortened irls saved in dictionary.
# Class accept long URL and return short URL.

import random
import string
import hashlib

class URLShortener:
    def __init__(self):
        self.shortener = {}

    def shorten(self, long_url):
        if long_url in self.shortener.values():
            print("URL already shortened")
            print(list(self.shortener.keys())[list(self.shortener.values()).index(long_url)])

        hash_object = hashlib.md5(long_url.encode())
        short_url = hash_object.hexdigest()[:6]
        
        self.shortener[short_url] = long_url

        return short_url

    def redirect(self, short_url):
        return self.shortener[short_url] if short_url in self.shortener.keys() else "URL not found"
    
if __name__ == "__main__":
    shortener = URLShortener()
    long_url = "https://www.google.com"
    short_url = shortener.shorten(long_url)
    shortener.shorten("https://www.example.com")
    shortener.shorten("https://www.example.com")
    shortener.shorten("https://www.example1.com")
    print(short_url)
    print(shortener.redirect(short_url))
    print(shortener.redirect("wrong_url"))
    print(shortener.shorten(long_url))
    print(shortener.shortener)