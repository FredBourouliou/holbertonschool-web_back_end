#!/usr/bin/env python3
"""
Async Generator module
"""
import asyncio
import random
from typing import Generator, AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    A coroutine that yields 10 random numbers between 0 and 10,
    with a 1 second delay between each yield.

    Returns:
        AsyncGenerator yielding random float values between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
