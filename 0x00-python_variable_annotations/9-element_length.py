#!/usr/bin/env python3
"""Annotate the below functions parameters
    and return values with the appropriate
    types
"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) ->\
        typing.Tuple[typing.Sequence, int]:
    """return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
