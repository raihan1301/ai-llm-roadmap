#******************* without asyncio **************************#

# import time

# def count():
#     print("one")
#     time.sleep(1)
#     print("two")
#     time.sleep(2)

# def main():
#     for _ in range(3):
#         count()

# if __name__ == "__main__":
#     start = time.perf_counter()
#     main()
#     elapsed = time.perf_counter() - start
#     print (f"{__file__} executed in {elapsed:0.2f} seconds. ")


"""
The count() function prints One and waits for a second, then prints Two and waits for another second. 
The loop in the main() function executes count() three times.
"""

#****************************************************************#

import asyncio
import time

async def count():   # if you want any method to be async use the keyword async
    print("one")
    await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(2)

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start

    print (f"{__file__} executed in {elapsed:0.2f} seconds. ")

"""
Now, you use the async keyword to turn count() into a coroutine function that prints One, waits for one second, then prints Two, and waits another second. 
You use the await keyword to await the execution of asyncio.sleep(). 
This gives the control back to the program’s event loop, saying: I will sleep for one second. Go ahead and run something else in the meantime.

The main() function is another coroutine function that uses asyncio.gather() to run three instances of count() concurrently. 
You use the asyncio.run() function to launch the event loop and execute main().

async def g():
    result = await f()  # Pause and come back to g() when f() returns
    return result

"""

"""
Example of what is valid and not valid

async def f(x):
    y = await z(x)  # Okay - `await` and `return` allowed in coroutines
    return y

async def g(x):
    yield x  # Okay - this is an async generator

async def m(x):
    yield from gen(x)  # No - SyntaxError

def n(x):
    y = await z(x)  # No - SyntaxError (no `async def` here)
    return y

"""

