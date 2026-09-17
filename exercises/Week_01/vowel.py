def main():
    word = input("enter your word: ")
    result = vowel_counter(word)
    print(result)

def vowel_counter(word):
    counter = 0

    for n in word:
        if n.lower() in ('a','e','i','o','u'):
            counter = counter + 1
    
    result = f"no of vowels in {word} = {counter}"
    return result


if __name__ == "__main__":
    main()