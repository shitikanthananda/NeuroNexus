import os
clear = lambda: os.system('cls')
from art import logo
print(logo)


def add(n1, n2):
    """Add two numbers"""
    return n1 + n2


def subtract(n1, n2):
    """Subtract two numbers"""
    return n1 - n2


def multiply(n1, n2):
    """Multiply two numbers"""
    return n1 * n2


def divide(n1, n2):
    """Divide two numbers"""
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    num1 = float(input("Enter the first number = "))
    end = False
    while not end:
        for i in operations:
            print(i)

        symbol = input("Pick an operation from the line above : ")
        num2 = float(input("Enter the next number = "))

        operator = operations[symbol]
        answer = operator(num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")

        ask = input( f"Type 'Yes' to continue with {answer} and 'No' to start a new calculation : ").lower()
        if ask == "yes":
            num1 = answer
            clear()

        elif ask == "no":
            end = True
            clear()
            calculator()

    else:
        print("!! Invalid Operator !!")


calculator()
