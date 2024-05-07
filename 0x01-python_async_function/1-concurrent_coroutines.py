#!/usr/bin/env python3
'''
1-concurrent_coroutines.py
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return a list of floats of running wait_random n number of times

    Parameters
    ----------
    n: int
        number of times to run wait_random
    max_delay: int
        maximum delay each function call should have

    Returns
    -------
    List[float]
        a list of floats of the running wait_random functions
    """
    output: List[float] = [wait_random(max_delay) for a in range(n)]
    # use as_completed to run all functions at once
    return [
        # use await to get the result of the function
        await func
        # for function in the list of functions returned from as_completed
        for func in asyncio.as_completed(output)
    ]
