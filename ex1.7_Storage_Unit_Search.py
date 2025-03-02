# Problem 1.7: Storage Unit Search
# A storage unit business has reached out to you to build software to manage their storage units.
# Write a program that will help them document their inventory, and search it.
# Your program will have 2 stages: let the owner enter their inventory, and then allow him to search it.
# Your program will first ask the owner how many storage units he has
# Then for each unit it will ask him what item is stored  in that unit (a single word)
# Then it will ask him, how many searches he wants to perform
# Then for each search it will ask him to enter an item to search for 
# If the item is located in one of the storage units, print the storage unit number, otherwise print "this item was not found"

# Example run:

# $ python3.11 storage.py
# Hello, tell me how many storage units you have: 5
# What item is stored in storage unit 1: lawnmower
# What item is stored in storage unit 2: vase
# What item is stored in storage unit 3: couch
# What item is stored in storage unit 4: table
# What item is stored in storage unit 5: tv
# Done recording inventory. Now you can search your inventory
# How many searches do you want to do: 3
# What item do you want to search for ?: couch
# "couch" is located in storage unit 3
# What item do you want to search for ?: tv
# "tv" is located in storage unit 5
# What item do you want to search for ?: ladder
# Did not find "ladder" in any of the storage units
# Searching is complete. Goodbye


# Ask the owner how many storage units he has
storage_quant = int(input('Hello, tell me how many storage units you have: '))

# For each unit, ask owner what is stored in that unit
unit_list = [0] * storage_quant

for i in range(0, len(unit_list), 1):
    inventory = input(f'What item is stored in storage unit {i+1}: ')
    unit_list[i] = inventory

# print(f"{', '.join(map(str, unit_list))}")

#Ask how many searches owner wants to perform
search_quant = int(input('How many searches do you want to do: '))

def search(queery):
    for i in range(storage_quant):
        if queery == unit_list[i]:
            print(f'"{queery}" is located in storage unit {i+1}')
            return
        
    print(f'Did not find "{queery}" in any of the storage units')      

for i in range(search_quant):
    q = input('What item do you want to search for ?: ')
    search(q)

print('Searching is complete. Goodbye')