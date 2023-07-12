#!/usr/bin/env python3
"""measure the total runtime and return it"""
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the total runtime and return it"""
    start_time = asyncio.get_event_loop().time()

    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time

    return total_runtime
