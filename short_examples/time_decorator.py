import asyncio
import time
from functools import wraps

def checker(e_time=600):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            while time.time() - start_time < e_time:  # Run for 600 seconds
                result = await func(*args, **kwargs)
                if result:
                    print(f"Task executed at {time.strftime('%X')}")
                    break
                else:
                    print("Task failed")
                await asyncio.sleep(30)  # Wait for 30 seconds
        return wrapper
    return decorator


@checker(60)
async def my_async_task():
    print(f"Task executed at {time.strftime('%X')}")
    return False

# To run the decorated function in an asyncio loop:
async def main():
    await my_async_task()

# Run the asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())
