#defining the math functions

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


num1 = float(input("Enter first operand: "))
num2 = float(input("Enter second operand: "))

print("Calculator Menu")
print("---------------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Which option do you want to preform? ")

if choice == '1':
    print("The result of this operation is", add(num1, num2), ". Goodbye!")

elif choice == '2':
    print("The result of this operation is", subtract(num1, num2), ". Goodbye!")

elif choice == '3':
    print("The result of this operation is", multiply(num1, num2), ". Goodbye!")

elif choice == '4':
    print("The result of this operation is", divide(num1, num2), ". Goodbye!")

else:
    print("Invalid selection! Terminating program.")
