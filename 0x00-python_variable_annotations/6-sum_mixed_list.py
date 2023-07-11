#!/usr/bin/env python3

"""Takes a list as an argument and returns a float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ returns the sum of the mxd_lst variable"""

    return float(sum(mxd_lst))
