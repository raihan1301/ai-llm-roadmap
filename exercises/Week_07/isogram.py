def is_isogram(words):
    seen = set()

    for word in words.lower():
        if word.isalpha():
            """
            word.isalpha() is a Python string method.
            It checks: Is this character a letter?
            """
            if word in seen:
                return False

            seen.add(word)

    return True

def main():
    print(is_isogram("lumberjacks"))      # True
    print(is_isogram("background"))       # True
    print(is_isogram("six-year-old"))     # True
    print(is_isogram("eleven"))  # false

main()