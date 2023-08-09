#!/usr/bin/env python3
"""Import async_generator from task 0 then write a coroutine"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension - function that takes no arguments
    Return: 10 random numbers
    """
    rslt = [i async for i in async_generator()]
    return rslt