#!/usr/bin/env python3
"""Class BasicCache that inherits from BaseCaching
   and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Inherits from BaseCaching and is a caching system
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
