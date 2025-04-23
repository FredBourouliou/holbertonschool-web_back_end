#!/usr/bin/env python3
"""Module for calculating element lengths in an iterable."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate the length of each element in an iterable.

    Args:
        lst: Iterable containing sequences.

    Returns:
        List of tuples with each sequence and its length.
    """
    return [(i, len(i)) for i in lst] 