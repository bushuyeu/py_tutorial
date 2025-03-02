# Simple Calculator
# Write a python program that asks the user for two numbers. 
# The program then prints out three calculations for these two numbers. 
# The sum of these numbers, the difference, and the product.

# Example Program Run:

# $ python3.11 program.py
# Enter first number: 2
# Enter second number: 4
# The sum of the numbers:6
# The difference of the numbers: -2
# The product of the numbers:8

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"The sum of the numbers: {num1 + num2}")
print(f"The difference of the numbers: {num1 - num2}")
print(f"The product of the numbers: {num1 * num2}")