import math

def menu():
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Factorial")
    print("6. x raised to the power y")
    print("7. Logarithm (base 10)")
    print("8. Natural Logarithm (ln)")
    print("9. Quit")
    choice = input("Enter your choice (1-9): ")
    return choice

def addition():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

def subtraction():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

def multiplication():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

def division():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 // num2
        print(f"Result: {num1} / {num2} = {result}")

def factorial(num):
    if num < 0:
        print("Error: Factorial is not defined for negative numbers.")
        return None
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

def x_power_y():
    base = int(input("Enter the base (x): "))
    exponent = int(input("Enter the exponent (y): "))
    result = base ** exponent
    print(f"Result: {base} raised to the power of {exponent} = {result}")

def log():
    num = float(input("Enter a positive number: "))
    if num <= 0:
        print("Error: Logarithm is not defined for non-positive numbers.")
    else:
        result = math.log10(num)
        print(f"Result: log({num}) = {result}")

def ln():
    num = float(input("Enter a positive number: "))
    if num <= 0:
        print("Error: Natural log is not defined for non-positive numbers.")
    else:
        result = math.log(num)
        print(f"Result: ln({num}) = {result}")

def calculator():
    choice = menu()
    if choice == '1':
        addition()
    elif choice == '2':
        subtraction()
    elif choice == '3':
        multiplication()
    elif choice == '4':
        division()
    elif choice == '5':
        num = int(input("Enter a non-negative integer: "))
        result = factorial(num)
        if result is not None:
            print(f"Result: {num}! = {result}")
    elif choice == '6':
        x_power_y()
    elif choice == '7':
        log()
    elif choice == '8':
        ln()
    elif choice == '9':
        print("Goodbye!")
    else:
        print("Invalid choice. Please select a valid option.")
    
    if choice != '9':
        calculator()

if __name__ == "__main__":
    calculator()
