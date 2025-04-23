#!/usr/bin/env python3
"""Module for measuring runtime of async functions"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): maximum delay for each wait_random call

    Returns:
        float: average execution time per coroutine
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    return (end - start) / n
