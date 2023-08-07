import asyncio, random

async def wait_random(max_delay=10):
    result = random.uniform(1, max_delay)
    return result


