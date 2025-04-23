#!/usr/bin/env python3
"""Module for creating a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies a float by multiplier.

    Args:
        multiplier: Float to multiply by.

    Returns:
        Function that takes a float and returns a float.
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply 