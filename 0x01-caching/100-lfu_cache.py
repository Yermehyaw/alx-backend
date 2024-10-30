#!/usr/bin/env python3
"""LFUCache module. Defines a LFU caching algo using a dict

Modules imported: none

"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFU(Least Frequently Used) Caching

    Args:
    None

    Attributes:
    cache_data(dict): Stored cache data
    cache_count(dict): counts no of requests to data in cache

    """
    def __init__(self):
        """Instance initializer
        """
        super().__init__()
        self.cache_count = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if not key or not item:  # if either is None
            return

        value = self.cache_data.get(key)  # exceptions handled
        if value:  # key exists
            if value == item:
                return
            self.cache_count[key] = self.cache_count.get(key, 0) + 1
            self.cache_data.update({key: item})
            return

        # If cache limit is reached, delete a cache data obj to create space
        if len(self.cache_count) >= BaseCaching.MAX_ITEMS:
            # get key with the lowest int value
            least = min(
                self.cache_count,
                key=self.cache_count.get
            )

            del self.cache_count[least]
            del self.cache_data[least]
            print(f'DISCARD: {least}')

        # Add new key, item to cache_data and cache_count
        self.cache_count[key] = self.cache_count.get(key, 0) + 1
        self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key
        """
        if not key:  # if None
            return

        # updates the freq count of the key in cache
        try:
            self.cache_count[key] = self.cache_count[key] + 1
        except KeyError:
            pass

        return self.cache_data.get(key)  # most exceptions are already handled
