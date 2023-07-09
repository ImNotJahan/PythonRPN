import math

operators = ["*", "+", "-", "/", "**", "log()"]

# not a real stack but python is also not a real programming language so who cares
stack = []
lastAnswer = 0

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
    equation = input().split(" ")
    
    if(equation[0] == ""): break

    for part in equation:
        if(part in operators):
            sl = len(stack) # sl = stackLength
            
            stack[sl - 2] = operate(part, stack[sl - 2], stack[sl - 1])
            del stack[sl - 1] # first number is replaced with result, second is deleted
        elif(part == "_"): # ans key
            stack.append(lastAnswer)
        else:
            stack.append(float(part))

    lastAnswer = stack[0]
    print(lastAnswer)
    stack = []
