#!/usr/bin/env python3
'''
1-concurrent_coroutines.py
'''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates a task that runs the `wait_random` function once

    Parameters
    ----------
    max_delay : int
        The maximum delay the function call should have

    Returns
    -------
    asyncio.Task
        The task that runs `wait_random`

    """
    return asyncio.create_task(wait_random(max_delay))
