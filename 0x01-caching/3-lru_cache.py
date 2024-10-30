#!/usr/bin/env python3
"""LRUCache module. Defines a LIFO caching algo using a dict

Modules imported: BaseCaching, datetime

"""
from base_caching import BaseCaching
from datetime import datetime


class LRUCache(BaseCaching):
    """
    LRU(Least Recently Used) Caching

    Args:
    None

    Attributes:
    cache_data(dict): Stored cache data
    cache_time(dict): stores last access time of cache data

    """
    def __init__(self):
        """Instance initializer
        """
        super().__init__()
        self.cache_time = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if not key or not item:  # if either is None
            return

        value = self.cache_data.get(key)  # exceptions handled
        if value:  # key exists
            if value == item:
                return
            self.cache_time.update({key: datetime.now()})
            self.cache_data.update({key: item})
            return

        # cache limit is reached, delete a cache data object to create space
        if len(self.cache_time) >= BaseCaching.MAX_ITEMS:
            # get the earliest key in cache
            earliest = min(
                self.cache_time,
                key=self.cache_time.get
            )

            del self.cache_time[earliest]
            del self.cache_data[earliest]
            print(f'DISCARD: {earliest}')

        # Add new key, item to cache_data and cache_time
        self.cache_time.update({key: datetime.now()})
        self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key
        """
        if not key:  # if None
            return

        value = self.cache_time.get(key)
        if value:  # updates last-accessed-time
            self.cache_time[key] = datetime.now()

        # None is auto ret if key is not in cache data
        return self.cache_data.get(key)  # most exceptions are already handled
