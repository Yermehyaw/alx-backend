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
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Deletion resistant hypermedia pagination. Returns a dict of
        key-value pair describing the dataset, regardless of deletions
        """
        indexed_data = list(self.indexed_dataset().keys())
        total_indexes = len(indexed_data)
        end_idx = indexed_data[total_indexes - 1]

        if index:
            assert isinstance(index, int)
            assert index < total_indexes and index > 0

            data = self.__dataset[index: page_size - 1]

        else:
            index = 0

        if page_size < end_idx:
            next_index = page_size

        return {
            'index': index,
            'next_index': page_size,
            'page_size': page_size,
            'data': data
        }
