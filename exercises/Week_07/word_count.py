from collections import Counter
import re


def count_words(s: str):
    words = re.findall(
        r"[a-zA-Z0-9]+(?:'\w+)?",
        s.lower()
    )
    """
    find a word made of letters or numbers, and optionally allow an apostrophe followed by more word characters. 
    So it correctly treats normal words like hello, numbers like 123, mixed text like abc123, and contractions/possessives 
    like don't or john's as single words, while ignoring punctuation such as commas, periods, and exclamation marks.
    """

    return Counter(words)

def main():
    print(count_words("Hello hello world!"))

main()

"""
If you do not want to use Collection library, below is the code

def count_words(s: str):
    words = re.findall(
        r"[a-zA-Z0-9]+(?:'\w+)?",
        s.lower()
    )

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count
"""