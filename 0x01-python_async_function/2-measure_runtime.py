#!/usr/bin/env python3
'''
2-measure_runtime.py
'''
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Returns the average time it takes to run the function
    `wait_n(n, max_delay)` n times.

    Arguments:
        n: The number of times to run the function
        max_delay: The maximum delay each function call should have

    Returns:
        The average time it takes to run the function
    """
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.perf_counter() - start
    return end / n
