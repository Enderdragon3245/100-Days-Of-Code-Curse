#Functions with Outputs

def format_name(f_name, l_name):
    """This function take a first and last name and format it to return the title case"""
    if f_name == "" or l_name == "":
        return 
    formated = f_name.title()
    formated_l = l_name.title()

    return f"{formated} {formated_l}"

formated_String = format_name("angela", "ANGELA")
print(formated_String)

#Docstrings

#Calculator Part 1: Combining Dictionaries and Functions

def add(n1, n2):
    return n1 + n2

def Subtract(n1, n2):
    return n1 - n2

def Multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

Calc = {
    "+": add,

    "-": Subtract,

    "*": Multiply,

    "/": divide
}

num1 = int(input("What the first number?"))
num2 = int(input("What the second number?"))

for symbol in Calc:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")

calculation_function = Calc[operation_symbol]
answer = calculation_function(num1, num2)