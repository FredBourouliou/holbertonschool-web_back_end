#!/usr/bin/env python3
"""Module for concurrent coroutines"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    and returns list of all delays in ascending order.

    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): maximum delay for each wait_random call

    Returns:
        List[float]: list of delays in ascending order
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
