#!/usr/bin/env python3
""" An asynchronous coroutine that takes in an integer argument """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Delay between 0 and max_delay with a default value of 10 """
    new_rnd = random.uniform(0, max_delay)
    await asyncio.sleep(new_rnd)
    return new_rnd
