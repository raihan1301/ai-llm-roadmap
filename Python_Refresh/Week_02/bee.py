words = {"PAIR": 4, "HAIR" : 4,  "CHAIR" : 5, "GRAPHIC": 7}

def main():
    print("Welcome to the Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(words) > 0:
        print(f"{len(words)} words left")
        guess = input("guess a word: ")

        if guess == "GRAPHIC":
            words.clear()  # clear whole dict
            print("you have won")

        if guess in words.keys():
            points = words.pop(guess)  # remove the key-value
            # print(f"good job! you scored {words[guess]} points.")
            print(f"good job! you scored {points} points.")

main()

# to add into list you can use .append
# to remove use .remove
# use .extend to add more values in one time in list
# .insert("position no","value" ) ex .insert(1, raihan) : so adding at positon 1 raihan
