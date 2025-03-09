import asyncio
import os
from datetime import datetime
import random
import time
import functools
from typing import Callable, Any
import aiofiles
import threading
from concurrent.futures import ThreadPoolExecutor

def time_profile(func: Callable) -> Callable:
    """
    A decorator that profiles execution time of both sync and async functions
    """
    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        try:
            if asyncio.iscoroutinefunction(func):
                result = await func(*args, **kwargs)
            else:
                result = func(*args, **kwargs)
            return result
        finally:
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute")

    @functools.wraps(func)
    def sync_wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute")

    return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper


def save_data():
    """Synchronous version of save_data"""
    file_name = datetime.now().strftime("%Y%m%d-%H%M") + ".txt"
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    
    data = "\n".join(str(random.randint(1, 100)) for _ in range(10000000))
    
    with open(file_path, "w") as file:
        file.write(data)

async def async_save_data():
    """Asynchronous version of save_data"""
    print("Starting async save...")  # Added logging
    file_name = datetime.now().strftime("%Y%m%d-%H%M") + "_async.txt"
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    
    data = "\n".join(str(random.randint(1, 100)) for _ in range(10000000))
    
    async with aiofiles.open(file_path, "w") as file:
        await file.write(data)
    print(f"Async save completed: {file_name}")  # Added logging

def run_async_in_thread(coro_func):
    """Helper function to run async code in separate thread"""
    def wrapper():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            # Create the coroutine inside the thread
            coro = coro_func()
            loop.run_until_complete(coro)
        finally:
            loop.close()
    
    thread = threading.Thread(target=wrapper)
    thread.daemon = False  # Change to non-daemon so it completes before exit
    thread.start()
    return thread

@time_profile
def process_data_async():
    """Non-blocking version that fires async save and returns immediately"""
    thread = run_async_in_thread(async_save_data)  # Pass the function itself
    return "Started async save"

@time_profile
def process_data_sync():
    save_data()

if __name__ == "__main__":
    # Run sync version
    print("Running sync version")
    process_data_sync()
    print("End of sync version")
    print("*" * 50)
    
    # Run async version (fire and forget)
    print("Running async version")
    process_data_async()
    print("End of async version")
    
    # Keep main thread alive to let async operation complete
    print("Waiting for async operations to complete...")
    time.sleep(10)  # Increased sleep time to ensure completion




