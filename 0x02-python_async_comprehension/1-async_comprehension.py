#!/usr/bin/env python3
"""async_generator() async function"""

import typing


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """return the 10 random numbers."""
    return [i async for i in async_generator()]
