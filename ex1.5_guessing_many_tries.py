# Problem 1.5: Number Guessing with many tries
# Update your number guessing game from above, and make the following changes
# Generate a random number between 1 and 1000
# Allow the user to enter how many guesses he wants to have 
# Every time the user guesses a wrong number, give them a hint. If the guess is lower than the random number print "Wrong guess, the number is higher". If the guess is higher than the random number, print "wrong guess, the number is lower"
# At the end of the game print all the guesses the player has made (regardless if he won or lost).

# Example Program Run

# $ python3.11 program.py
# I know a random number between 1 and 1000. 
# How many guesses do you want to make?: 4
# Enter your guess: 500
# The number is higher
# Enter your guess: 750
# The number is lower
# Enter your guess: 700
# The number is higher
# Enter your guess: 710
# The number is higher
# You lost the game. The random number is 715
# Here are all the guesses you made: 500, 750, 700, 710

import random 

random_int = random.randint(1,1000)
print("I know a random number between 1 and 1000.")

guess_int = int(input("How many guesses do you want to make?: "))
guess_counter = 1
guess_list = []

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
    
while guess_counter <= guess_int:
    curr_guess = int(input("Enter your guess: "))
    guess_list.append(curr_guess)
    if compare(curr_guess):
        exit()
    guess_counter += 1

print(f"You lost. The random number is {random_int}")

print(f"Here are all the guesses you made: {', '.join(map(str, guess_list))}.")