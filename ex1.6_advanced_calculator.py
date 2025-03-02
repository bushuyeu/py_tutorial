# Problem 1.6: Advanced Calculator
# Ask the user how many numbers they want to enter
# Let the user enter that many numbers
# Then make the following calculations for the full set of numbers that was entered
# Sum
# Avg
# Min - smallest number
# Max - biggest number
# Paired sums: add each pair of adjacent numbers together. if the amount of numbers is odd, then leave the last number as is.
# Example 1:
# Entered numbers: 2, 5, 7, 9
# Paired sums: 7, 16
# Example 2:
# Entered numbers: 2, 5, 7, 9, 13
# Paired sums: 7, 16, 13

# $ python3.11 program.py
# How many numbers do you want to enter: 4
# Enter number: 2
# Enter number: 5
# Enter number: 7
# Enter number: 9
# Sum: 23
# Average: 5.75
# Min: 2
# Max: 9
# Paired Sums: 7, 16

# Ask the user how many numbers they want to enter
input_int = int(input("How many numbers do you want to enter: "))

input_counter = 1
input_list = []
paired_sums_list = []

# Let the user enter that many numbers
while input_counter <= input_int:
    curr_int = int(input("Enter number: "))
    input_list.append(curr_int)
    input_counter += 1

# Then make the following calculations for the full set of numbers that was entered

# Sum
sum = sum(input_list)
print(f"Sum: {sum}")

# Avg
avg = sum / len(input_list)
print(f"Average: {avg}")

# Min - smallest number
min = min(input_list)
print(f"Min: {min}")

# Max - biggest number
max = max(input_list)
print(f"Max: {max}")

# Paired sums: add each pair of adjacent numbers together. if the amount of numbers is odd, then leave the last number as is.
def paired_sum(lst):
    if len(lst) % 2 != 0:
        lst.append(0)

    for i in range(0, len(lst), 2):
        pair_sum = lst[i] + lst[i+1]
        paired_sums_list.append(pair_sum)
    
    return paired_sums_list

paired_sums_list = paired_sum(input_list)
print(f"Paired Sums: {', '.join(map(str, paired_sums_list))}")