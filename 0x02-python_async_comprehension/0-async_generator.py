#!/usr/bin/env python3
"""
    a coroutine, async_generator that
    takes no arguments.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """"
        coroutine will loop 10 times, for each time asynchronously wait 1 second, then yield 
        number at random and 10. Use the random module.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
