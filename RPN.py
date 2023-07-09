import math

operators = ["*", "+", "-", "/", "**", "log()"]

# not a real stack but python is also not a real programming language so who cares
stack = []

def operate(operation, num1, num2):
    if(operation == "+"):
        return num1 + num2
    elif(operation == "-"):
        return num1 - num2
    elif(operation == "*"):
        return num1 * num2
    elif(operation == "/"):
        return num1 / num2
    elif(operation == "**"):
        return num1 ** num2
    elif(operation == "log()"):
        return math.log(num1) / math.log(num2)

while True:
    # I use " " as I think it looks better, but switching to "," will make it easier to type in calculator
    equation = input().split(" ")
    
    if(equation[0] == ""): break

    for part in equation:
        if(part in operators):
            sl = len(stack) # sl = stackLength
            
            stack[sl - 2] = operate(part, stack[sl - 2], stack[sl - 1])
            del stack[sl - 1] # first number is replaced with result, second is deleted
        else:
            stack.append(float(part))

    print(stack[0])
    stack = []
