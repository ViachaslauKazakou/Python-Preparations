import asyncio
import random
import time
rnd = [random.randint(1,10) for _ in range(10)]
names = ["Alice", "Bob", "Charlie"]
repeated_names = names * 10  # Repeat the names 10 times
# Create an iterator from the shuffled list
name_iterator = iter(repeated_names[:10])

# Shuffle the list to randomize the order
random.shuffle(repeated_names)


async def say_hello(delay, name, semaphore):
    async with semaphore:
        await asyncio.sleep(delay)
        print(f"Hello, {name} after delay {delay} sec.")


async def main():
    semaphore = asyncio.Semaphore(1)
    tasks = [say_hello(i, next(name_iterator), semaphore) for i in rnd]
    # tasks = [
    #     say_hello(2, "Alice"),
    #     say_hello(1, "Bob"),
    #     say_hello(3, "Charlie"),
    # ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    print("Start")
    print(f"estimated time: {sum(rnd)}")
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(f"Excecution time: {time.time()-start_time}")
