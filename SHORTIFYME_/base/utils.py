# base/factory.py

import shortuuid
from urllib.parse import urlparse

class URLShortenerFactory:
    @staticmethod
    def create_shortener(strategy):
        if strategy == 'simple':
            return SimpleURLShortener()
        elif strategy == 'customized':
            return CustomizedURLShortener()
        else:
            raise ValueError("Invalid strategy for URL shortener")

class SimpleURLShortener:
    @staticmethod
    def generate_short_url(long_url):
        parsed_url = urlparse(long_url)
        domain = parsed_url.netloc
        path = parsed_url.path
        short_id = shortuuid.uuid()[:8]
        return f"http://{domain}/{short_id}"

class CustomizedURLShortener:
    @staticmethod
    def generate_short_url(long_url, custom_text):
        parsed_url = urlparse(long_url)
        domain = parsed_url.netloc
        path = parsed_url.path
        short_id = shortuuid.uuid()[:8]  
        return f"http://{domain}/{custom_text}/{short_id}"