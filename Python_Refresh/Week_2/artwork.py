import requests


def get_artworks(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": query, "limit": limit}
        )
        response.raise_for_status()

        print("response ",response)

    except requests.HTTPError:
        return []
    
    content = response.json()
    #print("content ",content)

    return [artist["title"] for artist in content["data"]]
