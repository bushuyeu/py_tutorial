# Name Printer

# Write a python program that asks the user for their first name and last name. 
# Then the program prints how their name would appear on a Driver License (last name, then first name), and on a letter address (First name, then last name).

# Example Program Run:
# $ python3.11 program.py
# Enter your first name: Aysa
# Enter your last name: Erdnieva
# On a Driver License your name would show as: Erdnieva Aysa
# On a Letter your name would show as: Aysa Erdnieva

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(f"On a Driver License your name would show as: {last_name} {first_name}")
print(f"On a Letter your name would show as: {first_name} {last_name}")