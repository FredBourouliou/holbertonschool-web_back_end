#!/usr/bin/env python3
"""Module for concurrent tasks"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns list of all delays in ascending order.

    Args:
        n (int): number of times to spawn task_wait_random
        max_delay (int): maximum delay for each task_wait_random call

    Returns:
        List[float]: list of delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
