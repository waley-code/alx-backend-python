#!/usr/bin/env python3
"""async_generator() async function"""

import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """async_generator() async function"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
