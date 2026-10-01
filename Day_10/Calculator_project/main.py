import art


def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    number_1 = float(input("What's the first number?: "))

    is_continue = True

    while is_continue:

        print("+\n-\n*\n/\n")
        operator = input("Pick an operation: ")
        number_2 = float(input("What's the next number?: "))
        answer = operations[operator](number_1,number_2)
        print(f"{number_1} {operator} {number_2} = {answer}")


        choice_continue = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation:").lower()

        if choice_continue == "y":
            number_1 = answer
        else:
            is_continue = False
            print("\n"*20)
            calculator()

calculator()