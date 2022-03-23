def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print("Welcome! This is a Simple Calculator!")
print("Please select an operation :")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
  
select = int(input("Select operation form (1, 2, 3, 4) : "))
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
  
if select == 1:
    print(number1, "+", number2, "=", add(number1, number2))
elif select == 2:
    print(number1, "-", number2, "=", subtract(number1, number2))
elif select == 3:
    print(number1, "*", number2, "=", multiply(number1, number2))
elif select == 4:
    print(number1, "/", number2, "=", divide(number1, number2))
else:
    print("Invalid input")
