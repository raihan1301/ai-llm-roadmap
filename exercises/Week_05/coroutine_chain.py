import asyncio
import random
import time

async def get_user_with_posts(userid):
    user = await fetch_user(userid)
    posts = await fetch_posts(user)

    return {
        "user": user,
        "posts": posts,
    }


async def fetch_user(userid):
    delay = random.uniform(0.5,2.0)

    print(f"User coro: fetching user by {userid=}...")
    await asyncio.sleep(delay)

    user = {"id": userid, "name": f"User{userid}"}
    print(f"User coro: fetched user with {userid=} (done in {delay:.1f}s).")

    return user

async def fetch_posts(user):
    delay = random.uniform(0.5,2.0)

    print(f"Post coro: retrieving posts for {user['name']}...")
    await asyncio.sleep(delay)

    posts = []

    for i in range(1,4):
        posts.append(f"Post {i} by {user['name']}")

        print(
        f"Post coro: got {len(posts)} posts by {user['name']}"
        f" (done in {delay:.1f}s):"
        )

    for post in posts:
        print(f" - {post}")

    return posts

async def main():
    user_ids = [1,2,3]
    start = time.perf_counter()

    coroutines = []

    for user_id in user_ids:
        coroutine = get_user_with_posts(user_id)  # here it will not directly run this function it will just create coroutine object
        coroutines.append(coroutine) # here we are creating list of corountine object we created above

    results = await asyncio.gather(*coroutines)   # * means we unpack the list and send the list var one by one to asyncio gather and here they will run the function getuserwithposts

    """
    for smaller version of line 51 to 57 we can write like this as well
    results = await asyncio.gather(
        *(get_user_with_posts(user_id) for user_id in user_ids)
    )
    """
    end = time.perf_counter()

    print(f"\n==> Total time: {end - start:.2f} seconds")

    print("\nFinal results:")

    for result in results:
        user = result["user"]
        posts = result["posts"]

        print(f"{user['name']}: {len(posts)} posts")

if __name__ == "__main__":
    random.seed(444)
    asyncio.run(main())


"""

In below example you can see count is directly called and do all the steps and return the value and it will be stored in list
but in asyncio if its called count , than it did not run directly, it will create a coroutine object first in for loop as you seen above
and then when you do asyncio gather it will run the function


def count(c):
    count_value = c
    return count_value

def main():
    val = [1,2,3,4]
    val_result = []
    for i in val:
        val_var = count(i)
        val_result.append(val_var)

    print(val_result)

"""