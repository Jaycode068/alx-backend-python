#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay=10):
    result = random.random() *  max_delay
    await asyncio.sleep(result)
    return result


