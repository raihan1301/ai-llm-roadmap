import requests

def main():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url, timeout=10)
    response.raise_for_status()   # this is used to raise an exception of any error happend in http

    print(f"response from url = {response}")

    posts = response.json()   # posts wil hold full data

    for post in posts[:5]:   # only 1st 5 posts
        print(post["title"])

if __name__ == "__main__":
    main()