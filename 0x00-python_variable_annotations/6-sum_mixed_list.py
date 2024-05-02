#!/usr/bin/env python3
'''
6-sum_mixed_list.py
'''
from functools import reduce
from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    ''' returns sum of all values of list '''
    return reduce(lambda a, b: a + b, input_list)
