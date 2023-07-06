#!/usr/bin/env python3
"""code with the correct duck-typed 
    nnotations:
"""
from types import NoneType
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> typing.Union[typing.Any, NoneType]:
    """code with the correct duck-typed annotations:"""
    if lst:
        return lst[0]
    else:
        return None
