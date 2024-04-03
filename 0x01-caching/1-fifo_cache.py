#!/usr/bin/evn python3
"""Class FIFOCache that inherits from BaseCaching
   and is a caching system
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """Inherits from BaseCaching and implements FIFO caching algorithm
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_first_key, _ = self.cache_data.popitem(False)
            print(f'DISCARD: {discard_first_key}')

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
