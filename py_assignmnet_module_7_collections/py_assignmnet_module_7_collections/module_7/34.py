# 8. Functions

# Write a Python program to create a calculator using functions.

def add(a, b):
    print("Addition =", a + b)

def sub(a, b):
    print("Subtraction =", a - b)

def mul(a, b):
    print("Multiplication =", a * b)

def div(a, b):
    print("Division =", a / b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

add(num1, num2)
sub(num1, num2)
mul(num1, num2)
div(num1, num2)