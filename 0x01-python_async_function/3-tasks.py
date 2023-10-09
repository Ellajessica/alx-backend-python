#!/usr/bin/env python3
"""do not create an asynchronous function, use regular function """
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    max_delay and returns a asyncio.Task
    regusyntax to do this) task_wait_random
    """
    return asyncio.create_task(wait_random(max_delay))
