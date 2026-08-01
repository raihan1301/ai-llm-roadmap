# Regular code
# def main():
#     name = input("whats your name ? ").strip()

#     if "," in name:
#         last, first = name.split(",")
#         name = f"{first} {last}"
    
#     print(f" hello, {name}")

# main()

import re

def main():
    name = input("whats your name ? ").strip()

    matches = re.search(r"^(.+), (.+)$", name)

    if matches:
        last, first = matches.group()
        name = f"{first} {last}"
    
    print(f"hello, {name}")

main()
