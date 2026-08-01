import re

def main():
    # username = url.replace("https://twitter.com/" "")  --> we can use to get username from url but it will give the word before https also
    # username = url.removeprefix("https://twitter.com/")  --> this will remove everything before string and including this string

    # username = re.sub(r"https://twitter.com/","", url)
    # username = re.sub(r"^(https?://)?(www\.)?twitter\.com/","", url)  # ? make s as optional, 

    # username = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)

    url = input("URL: ").strip()
    username = re.search(r"^https?://(www\.)?twitter\.com/([a-zA-z0-9_]+)", url, re.IGNORECASE)
    # this means re will search the particular format in url variable
    
    if username:
        print(f"Username: ", username.group(2))

main() 

# for hexa color code 
# pattern = r"^#[a-fA-F0-9]{6}$  ---> ^# means very first character is #, {6}$ means only 6 character
# match - re.search(pattern, code)