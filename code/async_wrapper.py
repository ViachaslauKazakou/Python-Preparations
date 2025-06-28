import asyncio
from functools import wraps

def async_generator_decorator(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        await asyncio.sleep(1)
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        async for item in func(*args, **kwargs):
            yield item
    return wrapper

@async_generator_decorator
async def foo():
    for x in range(5):
        yield x

async def main():
    async for x in foo():
        print(x)

asyncio.run(main())
