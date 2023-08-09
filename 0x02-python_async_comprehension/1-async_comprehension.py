#!/usr/bin/env python3
"""Import async_generator from task 0 then write a coroutine"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    The coroutine will collect 10 random numbers using an async
     then return the 10 random numbers.
    """
    reslts = [i async for i in async_generator()]
    return reslts