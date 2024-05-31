from base.models import bases
from .models import cards
from base.utils import URLShortenerFactory

class BaseBuilder:
    def __init__(self):
        self.base = bases()
    
    def set_url_short(self, long_url):
        shortener = URLShortenerFactory.create_shortener()
        self.base.url_s = shortener.generate_short_url(long_url)
        return self
    
    def build(self):
        return self.base

def create_card_with_short_url(long_url, tag=None):
    
    new_card = cards(url_l=long_url)
    if tag:
        new_card.tagName = tag
    
    
    builder = BaseBuilder()
    base = builder.set_url_short(long_url).build()
    base.save()
    
   
    new_card.base = base
    new_card.save()
    
    return new_card