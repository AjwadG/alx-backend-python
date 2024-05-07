#!/usr/bin/env python3
'''
2-measure_runtime.py
'''

from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measures the runtime of the async_comprehension function.

    It calls the async_comprehension function and returns
    the time it took to run it.

    Returns:
        the time it took to run the async_comprehension function.
    """
    start = perf_counter()
    # call the async_comprehension function
    await async_comprehension()
    # return the time it took to run the async_comprehension function
    return perf_counter() - start
