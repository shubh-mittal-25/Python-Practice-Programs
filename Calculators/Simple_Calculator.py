logo = r"""
 _____________________________
|  _________________________  |
| |                      0. | |
| |_________________________| |
|_____________________________|
| |  7  | 8   | 9   | |  +  | |
| |_____|_____|_____| |_____| |
| |  4  |  5  |  6  | |  -  | |
| |_____|_____|_____| |_____| |
| |  1  |  2  |  3  | |  x  | |
| |_____|_____|_____| |_____| |
| |  .  |  0  |  =  | |  /  | |
| |_____|_____|_____| |_____| |
|_____________________________|
"""

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(logo)
    accumulate = True
    num1 = float(input("What's the first number? : "))
    while accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What's the next number? : "))
        result = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")
        num1 = result
        should_continue = input(
            f"Type 'y' to continue calculating with , or type 'n' to start a new calculation : ").lower()
        print()
        if should_continue == 'n':
            accumulate = False
            print("\n" * 20)
            calculator()

calculator()