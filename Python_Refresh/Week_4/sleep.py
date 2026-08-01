# but what will happen if someone enter a long and big number it can ran out of memory
# and we do not have to print like all this on main function, so we can use generator
# yield is the keyword

def main():
    n = int(input("What is n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "Sheep " * i  # it means return 1 value at a time and for loop will continue and this give one data at time

if __name__ == "__main__":
    main()