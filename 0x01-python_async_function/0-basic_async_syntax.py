#!/usr/bin/env python3
'''
0-basic_async_syntax.py
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
        takes a value then sleeps for a ranomd value
        betwen 0 and the maxvalue then returns it
    '''
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
