#!/usr/bin/env python3
""" an asynch coroutine that takes in an integer argument """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    delay between 0 and max_delay
    max a default value of 10
    """
    new_rand = random.uniform(0, max_delay)
    await asyncio.sleep(new_rand)
    return new_rand
