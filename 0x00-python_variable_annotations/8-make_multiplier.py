#!/usr/bin/env python3
"""takes a float and return a function that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def multiply_float(number: float) -> float:
        return multiplier * number
    return multiply_float
