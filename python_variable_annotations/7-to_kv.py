#!/usr/bin/env python3
"""Module for creating a key-value tuple."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple from a string and a number.

    Args:
        k: String to use as the first element of the tuple.
        v: Integer or float to square for the second element.

    Returns:
        Tuple with string and squared number as float.
    """
    return (k, float(v ** 2))
