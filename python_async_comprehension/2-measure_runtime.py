#!/usr/bin/env python3
"""
Measure Runtime module
"""
import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather,
    measures the total runtime and returns it.

    The runtime is roughly 10 seconds because although we're running
    4 async_comprehension coroutines in parallel, each one still
    needs to wait for the async_generator to yield 10 values with
    a 1-second delay between each, resulting in a ~10 second total.

    Returns:
        float: total runtime in seconds
    """
    start_time = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.perf_counter()
    return end_time - start_time
