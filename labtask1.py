import math 
name= "ZAHRA TUL HUSSAN SYED"
rollno= "23108195"
result = name + " " + rollno
print(result)
def menu():
    print("\nMenu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    return input("Enter your choice: ")

def sum(x , y):
    z = x + y
    return z

def subtract(a, b):
    c = a - b
    return c

def multiply(d,f):
    g = d * f
    return g

def divide(p, q):
    if q == 0:
        return "can not be divided"
    return p / q

def factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers!"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def x_power_y(x, y):
    return x ** y

def log(x):
    if x <= 0:
        return "log for negative number not possible"
    return math.log10(x)

def natural_log(x):
    if x <= 0:
        return "Natural log for negative number not possible"
    return math.log(x)

def main():
    choice = menu()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if choice == '1':
        result = sum(num1, num2)
        print("The result of addition is",result)
    elif choice == '2':
        result = subtract(num1, num2)
        print("The result of subtraction is", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print("The result of multiplication is", result)
    elif choice == '4':
        result = divide(num1, num2)
        print("The result of division is", result)
    elif choice == '5':
         num = int(input("Enter a non-negative integer for factorial: "))
         result = factorial(num)
         print("The factorial is", result)
    elif choice == '6':
        result = x_power_y(num1, num2)
        print("{num1} raised to the power of {num2} is", result)

    elif choice == '7':
         x = float(input("Enter a positive number "))
         result = log(x)
         print("The logarithm (base 10) is:", result)

    elif choice == '8':
         x = float(input("Enter a positive number  "))
         result = natural_log(x)
         print("The natural log is:" , result)
    else:
        print("Invalid choice! Please try again.")
  
    main()
main()

