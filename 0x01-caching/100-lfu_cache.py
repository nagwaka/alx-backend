#!/usr/bin/env python3
"""Class LFUCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """Iherits from BaseCaching and implements LFU caching algorithm
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, mru_item):
        """Reorders items based on the most recently used item
        """
        max_pos = []
        mru_freq = 0
        mru_pos = 0
        insert_pos = 0
        for i, key_freq in enumerate(self.keys_freq):
            if key_freq[0] == mru_item:
                mru_freq = key_freq[1] + 1
                mru_pos = i
                break
            elif len(max_pos) == 0:
                max_pos.append(i)
            elif key_freq[1] < self.keys_freq[max_pos[-1]][1]:
                max_pos.append(i)
        max_pos.reverse()
        for pos in max_pos:
            if self.keys_freq[pos][1] > mru_freq:
                break
            insert_pos = pos
        self.keys_freq.pop(mru_pos)
        self.keys_freq.insert(insert_pos, [mru_item, mru_freq])

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_item, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_item)
                self.keys_freq.pop()
                print(f'DISCARD: {lfu_item}')
            self.cache_data[key] = item
            insert_index = len(self.keys_freq)
            for i, key_freq in enumerate(self.keys_freq):
                if key_freq[1] == 0:
                    insert_index = i
                    break
            self.keys_freq.insert(insert_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
