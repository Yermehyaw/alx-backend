#!/usr/bin/env python3
"""LIFOCache module. Defines a LIFO cachong algo using a dict

Modules imported: none

"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Caching

    Args:
    None

    Attributes:
    cache_data(dict): Stored cache data
    cache_index(list)

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

        value = self.cache_data.get(key)  # exceptions handled
        if value:  # key exists
            if value == item:
                return
            self.cache_index.append(key)
            self.cache_data.update({key: item})  # item diffs
            return

        if len(self.cache_index) == BaseCaching.MAX_ITEMS:
            last_added = cache_index.pop()
            del self.cache_data[last_added]
            print(f'DISCARD: {last_added}')

        self.cache_index.append(key)
        self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key
        """
        if not key:  # if None
            return

        return self.cache_data.get(key)  # most exceptions are already handled
