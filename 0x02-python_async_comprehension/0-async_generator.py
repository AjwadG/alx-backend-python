#!/usr/bin/env python3
'''
0-async_generator.py
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    This coroutine generates a sequence of values.

    It takes a value, then sleeps for a random value between 0 and 10 seconds
    then returns it.

    It does this for a total of 10 times.

    Returns:
        A list of 10 random float values between 0 and 10
    """
    for _ in range(10):
        # sleep for 1 seond
        await asyncio.sleep(1)
        # return a random float value between 0 and 10
        yield random.uniform(0, 10)
