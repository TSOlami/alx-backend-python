#!/usr/bin/env python3
"""Takes a list of floats as argument and returns their sum as a float"""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """Returns the sum of the float in the list"""
    return float(sum(input_list))
