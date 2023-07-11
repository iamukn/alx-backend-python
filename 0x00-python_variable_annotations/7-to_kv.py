#!/usr/bin/env python3

"""receives a string and a tuple and returns a tuple"""
from typing import Tuple, List, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple"""

    return (k, float(v**2))
