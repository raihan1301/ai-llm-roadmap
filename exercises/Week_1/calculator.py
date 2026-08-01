def main():
    number1 = input("enter your 1st number: ")
    number2 = input("enter your second number: ")
    sign = input("enter your function sign + , - , *, / : ")

    result = math(number1, number2, sign)
    print(f"{number1} {sign} {number2} = {result}")

def math(n1, n2, sign):
    
    if sign == "+":
        result = float(n1) + float(n2)
    if sign == "-":
        result = float(n1) - float(n2)
    if sign == "*":
        result = float(n1)* float(n2)
    if sign == "/":
        if float(n2) <=0:
            result = f"{n2} is invalid"
        else:
            result = float(n1) / float(n2)
    
    return result

if __name__ == "__main__":
    main()