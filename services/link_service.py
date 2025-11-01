from utils.utils_random import random_alfanum
import re

class LinkService:
    def __init__(self) -> None:
        self.short_link_to_real_link: dict[str, str] = {}

    def add_https(self, url: str) -> str:
        if not url.startswith(('http://', 'https://')):
            return 'https://' + url
        return url

    def valid(self, url: str) -> bool:
        pattern=r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]+'
        if re.match(pattern,url):
            return True
        else: return False

    def create_link(self, link: str) -> str:
        link=self.add_https(link)
        if not self.valid(link):
            raise ValueError("422")
        short_link = random_alfanum(5)
        self.short_link_to_real_link[short_link] = link

        return short_link

    def get_real_link(self, link: str) -> str | None:
        return self.short_link_to_real_link.get(link)