import asyncio

async def powers_of_two(stop=10):
    exponent = 0

    while exponent < stop:
        yield 2**exponent  # basically it returns the value to where the function is called but does not end the function , it will continue from here
        exponent += 1  # once the value is given from above step it will start from here
        await asyncio.sleep(0.2)  # simulate some async work


async def main():
    g = []

    async for i in powers_of_two(5):
        g.append(i)

    print(g)

    f = []

    async for j in powers_of_two(5):  # this async for is ask for value one at a time
        if not (j // 3 % 5):   # j//3 is floor division means 3 // 3 is 1 and 5//3 is also 1 6//3 is 2
            f.append(j)  # it only allows the value from if statement if answer is 0 (2//3 is 0 and 0 % 5 is 0 hence pass,  4//3 is 1 and 1%5 is 1 hence fail)

    print(f)

    """
    to make it in short for line 20 to 26 you can write
    
    f = [j async for j in powers_of_two(5) if not (j // 3 % 5)]
    print(f)

    The iteration itself is still sequential unless you introduce concurrency by using asyncio.gather().
    
    """


if __name__ == "__main__":
    asyncio.run(main())