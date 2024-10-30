#!/usr/bin/env python3
"""MRUCache module. Defines a LIFO cachong algo using a dict

Modules imported: none

"""


class BaseCaching():
    """BaseCaching defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))


class MRUCache(BaseCaching):
    """
    MRU Caching

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

            self.cache_data.update({key: item})  # item diffs
            return

        if len(self.cache_count) == BaseCaching.MAX_ITEMS:
            # get key with the highest int value
            most = max(
                self.cache_count,
                key=self.cache_count.get
            )
            # remove from count
            del self.cache_count[most]
            # remove from data
            del self.cache_data[most]
            print(f'DISCARD: {most}')

        self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key
        """
        if not key:  # if None
            return

        self.cache_count[key] = self.cache_count.get(key, 0) + 1
        return self.cache_data.get(key)  # most exceptions are already handled
