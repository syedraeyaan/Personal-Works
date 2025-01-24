print("\n Two number calculator \n")

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

print("\n")

def add(num1, num2):
    result = num1 + num2
    return result

def subtract(num1, num2):
    result = num1 - num2
    return result

def divide(num1, num2):
    result = num1 / num2
    return result

def multiply(num1, num2):
    result = num1*num2
    return result

def remainder(num1, num2):
    result = num1%num2
    return result

print("""Operations to choose:-
      +
      -
      /
      *
      % \n""")

operation = input("Enter the operation to perform: ")

if operation == "+":
    print(add(num1,num2))

elif operation == "-":
    print(subtract(num1,num2))

elif operation == "/":
    print(divide(num1,num2))

elif operation == "*":
    print(multiply(num1,num2))

elif operation == '%':
    print(remainder(num1,num2))

else:
    print("Invalid Operation")