#!/usr/bin/python3
"""
Return the start and end index of a paginated list

Modules imported: None

"""


def index_range(page: int, page_size: int):
    """Return the start and end index of a paginated list"""
    if page == 0 or page_size == 0:
        return tuple()
    # page is 3 and page size is 3, the length of the data set is 10 from 0-9
    start_index = (page - 1) * page_size
    end_index = (start_index - 1) + page_size

    return (start_index, end_index)
