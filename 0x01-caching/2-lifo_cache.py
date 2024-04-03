#!/usr/bin/env python3
"""Class LIFOCache that inherits from BaseCaching
   and is a caching system
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """Inherits from BaseCaching and implements LIFO from BaseCaching
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                discard_last_key, _ = self.cache_data.popitem(True)
                print(f'DISCARD: {discard_last_key}')
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
