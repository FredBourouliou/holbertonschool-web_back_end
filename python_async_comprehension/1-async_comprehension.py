#!/usr/bin/env python3
"""
Async Comprehension module
"""
from typing import List
from asyncio import gather

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension over
    async_generator and returns the 10 random numbers.

    Returns:
        List[float]: 10 random float values
    """
    return [i async for i in async_generator()]
