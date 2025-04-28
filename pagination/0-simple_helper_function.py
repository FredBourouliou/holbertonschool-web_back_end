#!/usr/bin/env python3
"""
Simple helper function module
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two containing start and end index
    corresponding to the range of indexes for those pagination parameters.

    Args:
        page (int): The current page number (1-indexed)
        page_size (int): The number of items per page

    Returns:
        Tuple[int, int]: A tuple containing the start and end indexes
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
