#!/usr/bin/env python3
""" BaseCaching module defines a BasicCache using a simple dict without
a cachig algorithm

Modules imported: none
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Cache data using a dict without any coe cachong algorithm

    Args:
    None

    Attributes:
    cache_data(dict): Where cache data is stored

    """
    def __init__(self):
        """Instance initializer
        """
        super().__init__()

    def print_cache(self):
        """ Print the cache
        """
        super().print_cache()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if not key or not item:  # if either is None
            return

        try:
            self.cache_data.update({key: item})
        except Exception:
            return

    def get(self, key):
        """ Get an item by key
        """
        if not key:  # if None
            return

        return self.cache_data.get(key)  # most exceptions are already handled
