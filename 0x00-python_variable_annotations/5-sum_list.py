#!/usr/bin/env python3
"""
     type-annotated function sum_list which
     takes a list input_list of floats as
     argument and returns their sum as a float.
"""


def sum_list(input_list: list[float]) -> float:
    """returns their sum as a float."""
    sum1: float = 0
    for d in input_list:
        sum1 += d
    return sum1
