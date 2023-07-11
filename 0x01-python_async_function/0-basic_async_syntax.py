#!/usr/bin/env python3
"""asynchronous returning
    coroutine
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous returns
        coroutine
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
