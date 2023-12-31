#!/usr/bin/env python3
"""
    returns total_time n.
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """returns total_time n. """
    start_time = time.time()

    async def main():
        await wait_n(n, max_delay)

    asyncio.run(main())

    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / n

    return average_time
