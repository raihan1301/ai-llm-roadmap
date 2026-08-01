number_to_display = {}

def main():
    for n in range(1,101):
        if n % 3 == 0 and n % 5 == 0:
            number_to_display[n] = "fizzbuzz"

        elif n % 3 == 0:
            number_to_display[n] = "fizz"

        elif n % 5 == 0:
            number_to_display[n] = "buzz"
    
    for number in number_to_display:
        print(f"{number}, {number_to_display[number]}")



# if we loop over dictionary like "for number in number_to_display:" this will loop over the key and store that value in number var
# if we have to loop over valyes we do number_to_display.values()
# if you want to store both key and value you can do for number, result in number_to_display.items()

main()