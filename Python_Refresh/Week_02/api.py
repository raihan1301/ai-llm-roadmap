import requests #to send requests for api

def main():

    response = requests.get("https://api.artic.edu/api/v1/artworks/search")
    print(response)   #200 means it worked

    content = response.json()
    # print(content) : full content will come

    for artwork in content["data"]:
        print(f"* {artwork['title']}")

    artist = input(" search the artist in institute of chicago: ")
    
    query = requests.get(
        "https://api.artic.edu/api/v1/artworks/search",
        {"q": artist}
    )

    query_content = query.json()
    for artist in query_content["data"]:
        print(f"* {artist['title']}")



main()