#!/usr/bin/env python3
"""takes a string k and an int OR float v as arguments and returns a tuple"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str,float]:
    """Returns a tuple with a str and float type"""
    return k,v * v
