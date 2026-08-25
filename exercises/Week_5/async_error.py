import asyncio

async def main():
    results = await asyncio.gather(
        coro_a(),
        coro_b(),
        coro_c(),
        return_exceptions=True
    )

    exceptions = []

    for e in results:
        if isinstance(e, Exception):
            exceptions.append(e)

    if exceptions:
        raise ExceptionGroup("Errors", exceptions)

"""
you have three coroutines that raise three different types of exceptions. 
In the main() function, you call gather() with the coroutines as arguments. 
You also set the return_exceptions argument to True so that you can grab the exceptions if they occur.
"""

async def coro_a():
    await asyncio.sleep(1)
    raise ValueError("Error in coro A")

async def coro_b():
    await asyncio.sleep(1)
    raise TypeError("Error in coro B")

async def coro_c():
    await asyncio.sleep(1)
    raise IndexError("Error in coro c")

if __name__ == "__main__":
    try:
        result = asyncio.run(main())

    except* ValueError as error_group:
        for error in error_group.exceptions:
            print(f"Value error handled: {error}")

    except* TypeError as error_group:
        for error in error_group.exceptions:
            print(f"Type error handled: {error}")

    except* IndexError as error_group:
        for error in error_group.exceptions:
            print(f"Index error handled: {error}")

"""
In this code, you wrap the call to asyncio.run() in a try block. 
Then, you use the except* syntax to catch the expected exception separately. 
In each case, you print an error message to the screen.
"""

"""
When you do not need separate handling by type:

if __name__ == "__main__":
    try:
        asyncio.run(main())

    except* Exception as error_group:
        print(f"{len(error_group.exceptions)} tasks failed:")

        for error in error_group.exceptions:
            print(f" - {type(error).__name__}: {error}")

"""