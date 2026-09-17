import re
def acronym(words):
    
    words = re.findall(
            r"[a-zA-Z0-9]+(?:'\w+)?",
            words.lower()
        )

    acro= ""
    for word in words:
        acro = acro + word[0]


    return acro.upper()

def main():
    print(acronym("As Soon As Possible"))
    print(acronym("Liquid-crystal display"))
    print(acronym("Thank George It's Friday!"))

main()