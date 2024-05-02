#!/usr/bin/env python3
'''
5-sum_list.py
'''
from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    ''' returns sum of all double value of list '''
    return reduce(lambda a, b: a + b, input_list)
