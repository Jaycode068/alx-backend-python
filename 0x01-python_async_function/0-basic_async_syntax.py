#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    result = random.random() *  max_delay
    await asyncio.sleep(result)
    return result


