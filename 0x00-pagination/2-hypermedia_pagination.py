#!/usr/bin/env python3
"""
Siple pagination implementation

Modules Imported:
csv: CSV file manipulation methods
math: mathematical operations
typing: types in python

"""
import csv
import math
from typing import List
from typing import Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get pages from dataset"""
        assert isinstance(page, int) and isinstance(page_size, int)

        assert page != 0 and page_size != 0

        assert page > 0 and page_size > 0

        self.dataset()
        self._data_size = len(self.__dataset)
        self._no_pages = (self._data_size + (page_size - 1)) // page_size

        if page > self._no_pages:
            return []

        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return self.__dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Hypermedia pagination, Returns a dict to the user showing
        more resources than just the one requested
        """
        data = self.get_page(page, page_size)

        hyper_dict = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': None,
            'prev_page': None,
            'total_pages': self._no_pages
        }

        if page < self._no_pages:
            hyper_dict['next_page'] = page + 1
        if page > 1:
            hyper_dict['prev_page'] = page - 1

        return hyper_dict
