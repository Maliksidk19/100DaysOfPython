from Files.calculator_art import logo

def sum(num1, num2):
    """Returns addition of 2 numbers"""
    return num1 + num2

def subt(num1, num2):
    """Returns subtraction of 2 numbers"""
    return num1 - num2

def prod(num1, num2):
    """Returns Product of 2 numbers"""
    return num1 * num2

def division(num1, num2):
    """Return Division of 2 numbers"""
    return num1 / num2

operators = {
    "+": sum,
    "-": subt,
    "*": prod,
    "/": division
}    

def calculator():
    print(logo)
    num1 = float(input("What's the first number: "))
    print("<<< Choose an operator >>>")
    for op in operators:
        print(op)
    operation = input("Pick an operation: ")
    num2 = float(input("What's the next number: "))
    answer = operators[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")
    cont_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    if cont_calc == "y":
        continuty = True
    while continuty:
        operation = input("Pick an operation: ")
        num3 = float(input("What's the next number: "))
        answer2 = operators[operation](answer, num3)
        print(f"{answer} {operation} {num3} = {answer2}")
        answer = answer2
        cont_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if cont_calc == 'n':
            continuty = False
            calculator()
    if cont_calc == 'n':
        continuty = False
        calculator()
        
calculator()