import asyncio
import time

async def main():
    task1 = asyncio.create_task(coro([10,5,2]))
    task2 = asyncio.create_task(coro([3,2,1]))

    print(f"{type(task1) = }")
    print(f"{task1.done() = }")

    print("Start:", time.strftime("%X"))
    result = await asyncio.gather(task1, task2)
    print("End:", time.strftime("%X"))

    print(f"Both tasks done: {all((task1.done(), task2.done()))}")
    return result


async def coro(numbers):
    await asyncio.sleep(min(numbers))
    return list(reversed(numbers))


if __name__ == "__main__":
    result = asyncio.run(main())

    print(f"result: {result}")

"""
This pattern includes a subtle detail you need to be aware of: if you create tasks with create_task() 
but don’t await them or wrap them in gather(), and your main() coroutine finishes, 
then those manually created tasks will be canceled when the event loop ends. You must await all tasks you want to complete.

"""

#.....................................................................#

"""
Alternatively, you can loop over asyncio.as_completed() to get tasks as they complete. 
In this below example, the main() function uses asyncio.as_completed(), 
which yields tasks in the order they complete, not in the order they were started.
"""

async def main():
    task1 = asyncio.create_task(coro([10, 5, 2]))
    task2 = asyncio.create_task(coro([3, 2, 1]))

    print("Start:", time.strftime("%X"))

    for task in asyncio.as_completed([task1, task2]):
        result = await task
        print(f'result: {result} completed at {time.strftime("%X")}')

    print("End:", time.strftime("%X"))
    print(f"Both tasks done: {all((task1.done(), task2.done()))}")

async def coro(numbers):
    await asyncio.sleep(min(numbers))
    return list(reversed(numbers))

if __name__ == "__main__":
    result = asyncio.run(main())

    print(f"result: {result}")