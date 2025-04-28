#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


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
        """
        Returns a dictionary with the following key-value pairs:
        - index: the current start index of the return page
        - next_index: the next index to query with
        - page_size: the current page size
        - data: the actual page of the dataset

        Args:
            index (int, optional): The start index. Defaults to None (0).
            page_size (int, optional): The page size. Defaults to 10.

        Returns:
            Dict: A dictionary with pagination information
        """
        indexed_data = self.indexed_dataset()

        # Default to index 0 if None is provided
        if index is None:
            index = 0

        # Verify index is in a valid range
        assert isinstance(index, int) and index >= 0
        assert index < len(self.dataset())

        # Prepare data for the current page
        data = []
        current_index = index

        # Get the data for the current page
        for _ in range(page_size):
            # If current_index exists in indexed_data, add it to data
            while (current_index not in
                    indexed_data and current_index < len(self.dataset())):
                current_index += 1

            # Break if we've reached the end of the dataset
            if current_index >= len(self.dataset()):
                break

            data.append(indexed_data[current_index])
            current_index += 1

        # Calculate the next index
        next_index = current_index

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
