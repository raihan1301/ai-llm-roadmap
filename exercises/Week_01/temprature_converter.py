def main():
    decision_input = input("Type C to convert Celsius to Farehnite or Type F for vice versa: ")
    result = decision(decision_input)

    print(f" your temprature converts to {result}")


def decision(decision):
    temprature = float(input("enter your temprature you want to convert? "))

    if decision.lower() == "c":
        result = c_to_f(temprature) 
    elif decision.lower() == "f":
        result = f_to_c(temprature) 
    else:
        result = "Invalid Choice"
    
    return result

def c_to_f(temp):
    result = (temp * (9/5)) + 32
    return result

def f_to_c(temp):
    result = (temp - 32) * (5/9)
    return result

main()