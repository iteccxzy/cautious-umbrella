import asyncio
import time

'''
The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.

'''

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"incio a: {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"fin a: {time.strftime('%X')}")

asyncio.run(main())
