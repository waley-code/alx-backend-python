#!/usr/bin/env python3
"""Annotate the below functions parameters
    and return values with the appropriate
    types
"""
import typing

v = typing.List[typing.Tuple[typing.Sequence, int]]


def element_length(lst: typing.Iterable[typing.Sequence]) -> v:
    """
        return values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
