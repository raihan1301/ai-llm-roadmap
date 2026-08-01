# this will teach how to create own module and package by artwork.py

import artwork

def main():
    artwork_input = input("Artwork: ")
    artworks = artwork.get_artworks(query=artwork_input, limit=10)

    print("print ", artworks)
    for art_work in artworks:
        print(f"* {art_work}")

main()

# now you can create package (folder) as well which contains differnt modules (files)
# each package should have __init__.py file which says the computer this is package

# now to import we can do "import museum."module name""