#!/usr/bin/env python3
"""
async_comprehension from the previous
file and write a measure_runtime
 coroutine gather.
"""
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime would measure
    the total runtime and definitely return it.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
