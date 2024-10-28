#!/usr/bin/env python3
"""
Return the start and end index of a paginated list

Modules imported: typing

"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the start and end index of a paginated list"""
    if page == 0 or page_size == 0:
        return tuple()
    # page is 3 and page size is 3, the length of the data set is 10 from 0-9
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
