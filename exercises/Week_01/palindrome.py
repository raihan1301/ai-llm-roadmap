def main():
    word_input = input("enter your word to check if reverse is same or not: ")
    result = palindrome(word_input)
    print(result)

def palindrome(input):

    word = []
    reverse_word = []

    for letter in input:
        word.append(letter)
    for letter in reversed(word):   # reveresed key word to read the list from backwards
        reverse_word.append(letter)

    if word == reverse_word:
        result = "word reads same forwards and backward"
    else:
        result = "word does not read same"
    
    return result

main()