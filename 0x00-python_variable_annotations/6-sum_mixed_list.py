#!/usr/bin/env python3
"""Takes a list of floats as argument and returns their sum as a float"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Returns the sum of the float in the list"""
    return float(sum(mxd_lst))
