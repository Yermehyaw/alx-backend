#!/usr/bin/env python3
"""FIFOCache module. Defines a FIFO cachong algo using a dict

Modules imported: none

"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Cacheing

    Args:
    None

    Attributes:
    cache_dat(dict): Stored cache data

    """
    def __init__(self):
        """Instance initializer
        """
        super().__init__()
        self.cache_index = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if not key or not item:  # if either is None
            return

        # test key, item if they are already part of cache
        value = self.cache_data.get(key)  # exceptions handled
        if value:  # key exists
            if value == item:
                return
            self.cache_index.append(key)
            self.cache_data.update({key: item})  # item diffs
            return

        if len(self.cache_index) == BaseCaching.MAX_ITEMS:
            first_added = self.cache_index[0]
            del self.cache_index[0]
            del self.cache_data[first_added]
            print(f'DISCARD: {first_added}')

        self.cache_index.append(key)
        self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key
        """
        if not key:  # if None
            return

        return self.cache_data.get(key)  # most exceptions are already handled
