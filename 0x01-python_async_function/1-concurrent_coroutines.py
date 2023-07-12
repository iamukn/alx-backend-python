#!/usr/bin/env python3

"""A coroutine"""


import asyncio
import random
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    res = []
    for i in range(n):
        data = wait_random(max_delay)
        res.append(data)

    for task in asyncio.as_completed((res)):
        delay = await task
        delays.append(delay)
    return delays
