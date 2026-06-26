#!/usr/bin/env python3
"""Module that defines task_wait_n coroutine"""
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns task_wait_random n times and returns delays in ascending order"""
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in tasks:
        delay = await task
        inserted = False
        for i in range(len(delays)):
            if delay < delays[i]:
                delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            delays.append(delay)

    return delays
