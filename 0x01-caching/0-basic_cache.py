#!/usr/bin/env python3
""" BaseCaching module
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
        if not key or not item:  # if either is None
            return

        return self.cache_data.get(key)  # most exceptions are already handled


class BaseCache(BaseCaching):
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
        """Add an item in the cache
        """
        super().put(key, item)

    def get(self, key):
        """ Get an item by key
        """
        super().get(key)
