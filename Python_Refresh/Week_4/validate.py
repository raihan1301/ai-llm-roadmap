import re  #regex library

def main():
    email = input("what is your email").strip()

    # if re.search(r".+@.+\.", email):  # ".+" means any character before @  # and same @ .+ after this you can this ..*@..* use r for raw 
    # if re.search(r"^[^@]+@[^@]+\.edu$"):  #+@ before this means not @ so there cannot be multiple @
    if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]", email):  #+@ before this means not @ so there cannot be multiple @
        print("valid")
    else:
        print("invalid")

main()    


# if we want to specific we can do domain.endswith(".com")
# \w = word character