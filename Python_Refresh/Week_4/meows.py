# def meow(n):
#     for _ in range(n):
#         print(meow)

# number = input("Number: ")   # now if someone enter 3 it will be string and string cannot be in range hence it will give error
# meow(number)


def meow(n: int) -> None:   # this is type hint and hence python will know it is int if we run in mypy
    for _ in range(n):
        """
        Meow n times
        """
        print(meow)

number = input("Number: ")   # now if someone enter 3 it will be string and string cannot be in range hence it will give error
meow(number)