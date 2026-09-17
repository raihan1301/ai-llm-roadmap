import asyncio
import aiohttp

async def main():
    websites = [
        "https://realpython.com",
        "https://pycoders.com",
        "https://www.pythong.org"
    ]

    # await asyncio.gather(*(check(url) for url in websites))
    coroutines = []

    for url in websites:
        coroutine = check(url)
        coroutines.append(coroutine)

    await asyncio.gather(*coroutines)

async def check(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"{url}: status -> {response.status}")

"""
The async with statement ensures that both ClientSession and the individual HTTP response are properly and asynchronously managed 
by opening and closing them without blocking the event loop.

main() runs the check() coroutines concurrently, allowing you to fetch the URLs in parallel 
without waiting for one to finish before starting the next. gather function

"""

if __name__ == "__main__":
    asyncio.run(main())