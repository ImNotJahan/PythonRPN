import math

OPERATIONS = ["*", "+", "-", "/", "**", "**-", "%", "log()",
              "==", "!=", ">", ">=", "<", "<=", "and", "or",
              "=", "+=", "-=", "*=", "/=", "%=", "**="]
FUNCTIONS = ["sin()", "cos()", "tan()", "asin()", "acos()", "atan()",
             "radians()", "degrees()", "**2", "**-1", "not",
             "++", "--"]

variables = {}

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
    elif(operation == "**-"):
        return num1 ** (1 / num2)
    elif(operation == "%"):
        return num1 % num2
    elif(operation == "log()"):
        return math.log(num1) / math.log(num2)
    elif(operation == "=="):
        return num1 == num2
    elif(operation == "!="):
        return num1 != num2
    elif(operation == ">"):
        return num1 > num2
    elif(operation == ">="):
        return num1 >= num2
    elif(operation == "<"):
        return num1 < num2
    elif(operation == "<="):
        return num1 <= num2
    elif(operation == "and"):
        return num1 and num2
    elif(operation == "or"):
        return num1 or num2
    elif(operation == "="):
        variables[num1] = num2
        print(variables)
        return None
    elif(operation == "+="):
        variables[num1] = variables[num1] + num2
        return None
    elif(operation == "-="):
        variables[num1] = variables[num1] - num2
        return None
    elif(operation == "*="):
        variables[num1] = variables[num1] * num2
        return None
    elif(operation == "/="):
        variables[num1] = variables[num1] / num2
        return None
    elif(operation == "%="):
        variables[num1] = variables[num1] % num2
        return None
    elif(operation == "**="):
        variables[num1] = variables[num1] ** num2
        return None

def execute(function, num):
    if(function == "sin()"):
        return math.sin(num)
    elif(function == "cos()"):
        return math.cos(num)
    elif(function == "tan()"):
        return math.tan(num)
    elif(function == "asin()"):
        return math.asin(num)
    elif(function == "acos()"):
        return math.acos(num)
    elif(function == "atan()"):
        return math.atan(num)
    elif(function == "degrees()"):
        return math.degrees(num)
    elif(function == "radians()"):
        return math.radians(num)
    elif(function == "**-1"):
         return math.sqrt(num)
    elif(function == "**2"):
         return num ** 2
    elif(function == "not"):
        return not num;
    elif(function == "++"):
        variables[num] = variables[num] + 1
        return None
    elif(function == "--"):
        variables[num] = variables[num] - 1
        return None

while True:
    equation = input()

    if("," in equation): equation = equation.split(",")
    else: equation = equation.split(" ")
    
    if(equation[0] == ""): break

    for part in equation:
        sl = len(stack) # sl = stackLength
        
        if(part in OPERATIONS):
            stack[sl - 2] = operate(part, stack[sl - 2], stack[sl - 1])
            del stack[sl - 1] # first number is replaced with result, second is deleted
        elif(part in FUNCTIONS):
            stack[sl - 1] = execute(part, stack[sl - 1])
        elif(part in variables):
            stack.append(variables[part])
        elif(part == "_"): # ans key
            stack.append(lastAnswer)
        elif(part == "pi"):
            stack.append(math.pi)
        elif(part == "e"):
            stack.append(math.e)
        elif(part == "True"):
            stack.append(True)
        elif(part == "False"):
            stack.append(False)
        elif(part[:2] == "()"):
            stack.append(part[2:])
        else:
            stack.append(float(part))

        if(stack[-1] == None): del stack[-1]

    if(len(stack) > 0):
        lastAnswer = stack[0]
        print(lastAnswer)
        
    stack = []
