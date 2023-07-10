#!/usr/bin/env python3
'''
Test file for pait_n coroutine
'''
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    """wait_n except task_wait_random is """
    tasks = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)
    delays = await asyncio.gather(*tasks)
    delays.sort()
    return delays
