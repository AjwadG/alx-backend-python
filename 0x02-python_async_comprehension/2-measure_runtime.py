#!/usr/bin/env python3
'''
2-measure_runtime.py
'''

import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of the async_comprehension function.

    Returns:
        The time it took to run the async_comprehension function.
    """
    # start measuring the time
    start = perf_counter()

    # call the async_comprehension function four times in parallel
    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    # stop measuring the time and return the runtime
    return perf_counter() - start
