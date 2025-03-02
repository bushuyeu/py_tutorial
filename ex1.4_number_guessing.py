# Number guessing Game
# Write a python program that plays the number guessing game with the user. 
# At the beginning the program will generate a random number between 1 and 10.
# Then it will allow the user to enter a maximum of two guesses.
# For each guess if the guessed number is lower than the random number the program prints  "The number is lower" if the guessed number is higher than the random number the program prints  "The number is higher" if  the guessed number is the same as the random number the program prints "You won. You guessed the correct number" and the program exits

# If both guesses are wrong, the program prints the lost game message, and the random number that the user was trying to guess
# Example: "You lost the game. The random number is 5"

import random

random_int = random.randint(1,10)
print("I know a random number between 1 and 10. You have 2 guesses to figure out what it is.")

def compare(guess):
    if random_int > guess:
        print("The number is higher")
        return False
    elif random_int < guess:
        print("The number is lower")
        return False
    else:
        print("You won. You guessed the correct number")
        return True

guess1 = int(input("Enter your first guess: "))
if compare(guess1):
    exit()
guess2 = int(input("Enter your second guess: "))
if compare(guess2):
    exit()

print(f"You lost. The random number is {random_int}")