def main():
    query = input("Enter your word = ")
    response = Omit(query)
    print(response)

def Omit(text):
    vowels = "aeiou"
    result = ""

    for letter in text:
        if letter.lower() not in vowels:
            result = result + letter
    
    return result

main ()