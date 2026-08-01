def main():
    input_value = input("enter your vanity plate: ")
    if is_valid(input_value) == True:
        print("vanity plate is correct")
    else:
        print("vanity plate is not correct")

def is_valid(plate):
    
    if not 2 <= len(plate) <= 6:
        return False

    if not plate[:2].isalpha():  # is alpha will check if first 2 are character if yes returns true and it will not go inside
        return False  # if .isalpha return false and not false is true hence it will go inside the if statement and return False
    
    if not plate.isalnum():  # is alnum check only letter and number is there
        return False
    
    number_started = False

    for character in plate:
        if character.isdigit():  #if in that loop that character is digit or not, if yes it will go inside
            if not number_started and character == "0":  # if character is 0 and "number _started is false" hence not number_started become true
                return False # as it is true it will come inside if statement and return false
            number_started = True
        
        elif number_started:  # this means it will enter if number started is true and alphabet comes in
            return False
    
    return True

if __name__ == "__main__":
    main()

#explnation
# as character enter the loop it will first get checked with if statement and once number_started becomes true
# now next character comes in if its number it will go to if and than exit because it already went to if so it will not move to elif
# now next character comes in if its alphabet it will not go in if, it will go inside elif and number-staretd is true it will be become return false
# no character allowed after number