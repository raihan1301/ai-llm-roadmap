import asyncio
import random

COLORS = (  # this is like tuple if delay is one which is COLORS[1] it will be cyan color
    "\033[0m",  # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)


async def makerandom(delay, threshold=6):
    color = COLORS[delay]
    print(f"{color}Initiated makerandom({delay}).")

    number = random.randint(0,10)
    while number <= threshold:
        print(f"{color}makerandom({delay}) == {number} too low; retrying.")
        await asyncio.sleep(delay)
        number = random.randint(0,10)

    print(f"{color}---> Finished: makerandom({delay}) == {number}" + COLORS[0])
    return number


async def main():
    return await asyncio.gather(  #it is like 3 worker and all work individually does not wait for each other
        makerandom(1,9),  # this will pass the delay and threshold, so for example delay 1 sec and threhold is 9 so if random number generated above should be greater than 9
        makerandom(2,8),  # makerandom is corountine function
        makerandom(3,8),
    )


if __name__ == "__main__":
    random.seed(444)

    r1, r2, r3 = asyncio.run(main())  # this means run the main and assign the values of that 3 workers in r1,r2,r3
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")


"""
Most programs will consist of small, modular coroutines and a wrapper function that serves to chain each smaller coroutine

>>> import asyncio

>>> async def main():
...     print("Hello...")
...     await asyncio.sleep(1)
...     print("World!")
...

>>> routine = main()
>>> routine
<coroutine object main at 0x1027a6150>

In this example, calling main() directly returns a coroutine object that you can’t use in isolation. 
You need to use asyncio.run() to schedule the main() coroutine for execution on the event loop:

>>> asyncio.run(routine)

"""