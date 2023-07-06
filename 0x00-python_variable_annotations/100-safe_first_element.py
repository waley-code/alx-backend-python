#!/usr/bin/env python3
"""code with the correct duck-typed
    nnotations:
"""
from types import NoneType
import typing


v = typing.Union[typing.Any, NoneType]


def safe_first_element(lst: typing.Sequence[typing.Any]) -> v:
    """
    code with the correct duck-typed annotations:
    """
    if lst:
        return lst[0]
    else:
        return None
