#!/usr/bin/env python3

""" Python Async function"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """async function that sleeps for 10 secs and returns
    its  sleep value """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
