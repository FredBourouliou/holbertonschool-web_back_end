#!/usr/bin/env python3
"""
return a random number
"""
import asyncio
import random
from typing import Generator, AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """return a random number"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)