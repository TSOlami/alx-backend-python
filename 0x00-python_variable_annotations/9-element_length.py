#!/usr/bin/env python3
"""Annotate a given function’s parameters"""
from typing import List, Sequence, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return the list of items"""
    return [(i, len(i)) for i in lst]
