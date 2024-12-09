'''
Task 2:
Write a program that asks the user to input a string, then choose a keyboard, then plans the actions of Robbie the robot 
so that it can type this string on a keyboard.
For a given input string,
If there is a single keyboard on which in can be typed, then Robbie picks that one.
If it can be typed on multiple keyboards, Robbie picks a single keyboard as follows:
The one that requires the fewest moves, or, if there is a tie, 
The first best keyboard configuration (in the order we give them).
Finally, there may not be a keyboard that can type that string.
The keyboards have the configurations below.
Configuration 0
abcdefghijklm
nopqrstuvwxyz
Configuration 1
789
456
123
0.-
Configuration 2
chunk
vibex
gymps
fjord
waltz
Configuration 3
bemix
vozhd
grypt
clunk
waqfs
Robbie starts at the top left position of the chosen keyboard.
'''

'''
This program prompts user to
enter a string, chooses one keyboard 
configuration with the least steps
and output the steps
'''

configurations = [
    ["abcdefghijklm", "nopqrstuvwxyz"],
    ["789", "456", "123", "0.-"],
    ['chunk', 'vibex', 'gymps', 'fjord', 'waltz'],
    ['bemix', 'vozhd', 'grypt', 'clunk', 'waqfs']
]

#setting the initial condition to False to be changed later if string can be typed out by one of the configurations
in_configuration = False

#list to store number of steps in each configuration
steps_count = []
word = input("Enter a string to type: ")

# calculate steps for each configuration
for configuration in configurations:
    current_row, current_column = 0, 0  # reset start position for each configuration
    total_steps = 0
    for letter in word:
        # setting the initial condition to false to be changed if the letter in the string can be found
        found = False
        for row in range(len(configuration)):  #loop though the total number of rows
            for column in range(len(configuration[0])):  #loop through the total number of columns
                if configuration[row][column] == letter:
                    found = True
                    #counting the total steps needed 
                    horizontal = abs(column - current_column)
                    vertical = abs(row - current_row)
                    total_steps += horizontal + vertical
                    current_column = column
                    current_row = row
                    break
            if found:
                break
        if not found:
            break 
    if found:
        #appending the total number of steps to a list if a configuration is found
        steps_count.append(total_steps)
        in_configuration = True
    else:
        #appending infinity value to a list if configuration is not found
        steps_count.append(float('inf')) 

if not in_configuration:
    print("The string cannot be typed out.")
else:
    # choose a configuration with the minimum steps by matching the index of lists steps_count and configurations
    min_steps = min(steps_count)
    chosen_configuration = configurations[steps_count.index(min_steps)]
    
    print("Configuration used:")
    print("-" * (max(len(row) for row in chosen_configuration) + 4))
    for row in chosen_configuration:
        print("|", row, "|")
    print("-" * (max(len(row) for row in chosen_configuration) + 4))

    #performing operation based on the chosen configuration 
    current_column,current_row = 0, 0  #setting the initial pointer position to top left
    steps = []
    print("The robot must perform the following operations:")
    for letter in word:
        for row in range(len(chosen_configuration)):
            for column in range(len(chosen_configuration[0])):
                if chosen_configuration[row][column] == letter:
                    #finding horizontal and vertical movements needed
                    horizontal = column - current_column
                    vertical = row - current_row
                    # resetting the new initial position to the current position
                    current_column = column
                    current_row = row
                    break
            if chosen_configuration[row][column] == letter:
                break
        
        #appending the steps
        if horizontal > 0:
            steps.extend(["r"] * horizontal)
        elif horizontal < 0:
            steps.extend(["l"] * abs(horizontal))
        if vertical < 0:
            steps.extend(["u"] * abs(vertical))
        elif vertical > 0:
            steps.extend(["d"] * vertical)
        steps.append("p")
    
    #output the steps
    for step in steps:
        print(step, end="")
    print() 




