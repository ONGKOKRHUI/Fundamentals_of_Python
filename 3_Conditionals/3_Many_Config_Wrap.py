'''
Task 3:
Write a program that asks the user to input a string, then choose a keyboard, then plans the actions of Robbie the robot so that it can type this string on a keyboard.
This time, though, Robbie is able to wrap around the keyboard. For example:
In the row "abcde", Robbie can move from 'a' to 'e' in 1 move to the left. This move is encoded as "lw", where "w" marks a wrap (horizontal or vertical).
In the row "abcde", Robbie can move from 'e' to 'a' in 1 move to the right. This move is encoded as "rw".
The same applies for columns. The character 'w' is also used to mark vertical wrapping.
Proud of this new technique, and for style points, Robbie uses wrapping whenever it does not increase the number of moves required. This means that, for example,
in the row "ab", to go from 'a' to 'b', Robbie will always prefer doing "lw" than "r" ('w' does not count as a move). 
The other rules and keyboard configurations are the same as in Task 2.
'''

'''
This program prompts user to
enter a string, chooses one keyboard 
configuration with the least steps, allowing
the computer to wrap around the keyboard
and output the steps
'''

configurations = [
    ["abcdefghijklm", "nopqrstuvwxyz"],
    ["789", "456", "123", "0.-"],
    ['chunk', 'vibex', 'gymps', 'fjord', 'waltz'],
    ['bemix', 'vozhd', 'grypt', 'clunk', 'waqfs']
]

#function to determine the shortest horizontal movement and append the steps to the output list
def find_horizontal(column, current_column):
    if column > current_column:  # object is at the right of the current position
        if max_column - (column - current_column) <= column - current_column:  #wrapping steps to the left is shorter
            for left in range(current_column):
                output.append("l")
            output.append("lw")
            for left in range(max_column-(column+1)):
                output.append("l")
        else:      #usual path to the right is shorter
            output.extend(["r"] * (column -current_column))
    elif current_column > column:          # object is at the left of the current position
        if max_column - abs(column - current_column) <= abs(column- current_column):  #wrapping steps to the right is shorter
            for right in range(max_column-(current_column+1)):
                output.append("r")
            output.append("rw")
            for right in range(column):
                output.append("r")
        else:      #usual path to the left is shorter
            output.extend(["l"] * abs(column - current_column))


#function to determine the shortest vertical movement and append the steps to the output list
def find_vertical(row,current_row):
    if row > current_row:  # object is below the current position
        if max_row - (row - current_row) <= row - current_row:  # wrapping steps up is shorter
            for down in range(current_row):
                output.append("u")
            output.append("uw")
            for down in range(max_row - (row+1)):  
                output.append("u")
        else:      #normal path down is shorter
            output.extend(["d"] * (row - current_row))
    elif row < current_row:  # object is above the current position
        if max_row - abs(row - current_row) <= abs(row - current_row):  # wrapping steps down is shorter
            for down in range(max_row-(current_row+1)):
                output.append("d")
            output.append("dw")
            for down in range(row):
                output.append("d")
        else:    # wrapping steps up is shorter
            output.extend(["u"] * abs(row - current_row))


#setting condition to False which can be changed when a configuration can type out the string
in_configuration = False
steps_count = []
word = input("Enter a string to type: ")

# calculate steps for each configuration
for configuration in configurations:
    max_rows = len(configuration)  #maximum number of rows
    max_columns = len(configuration[0])  #maximum number of columns
    current_row, current_column = 0, 0  # resetting start position for each configuration
    total_steps = 0  
    for letter in word:
        found = False   #setting found condition to false which can be changed to true when the letter is found
        for row in range(max_rows):
            for column in range(max_columns):
                if configuration[row][column] == letter:
                    found = True
                    #comparing the number of steps for horizontal normal path and wrapped path
                    if max_columns - abs(column - current_column) <= abs(column - current_column):
                        horizontal = max_columns - abs(column - current_column)
                    else:
                        horizontal = abs(column - current_column)
                    #comparing the number of steps for vertical normal path and wrapped path
                    if max_rows - abs(row - current_row) <= abs(row - current_row):
                        vertical = max_rows - abs(row - current_row)
                    else:
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
        #appending the number of steps for each configuration (if available)
        steps_count.append(total_steps)
        in_configuration = True
    else:
        #appending infinity value for unsuitable configurations 
        steps_count.append(float('inf'))  

if not in_configuration:
    print("The string cannot be typed out.")
else:
    #choosing the configuration with the minimum steps by matching the index of lists steps_count and configurations
    min_steps = min(steps_count)
    chosen_configuration = configurations[steps_count.index(min_steps)]
    
    print("Configuration used:")
    print("-" * (max(len(row) for row in chosen_configuration) + 4))
    for row in chosen_configuration:
        print("|", row, "|")
    print("-" * (max(len(row) for row in chosen_configuration) + 4))

    #main code to perform the operation on the chosen configuration
    current_row, current_column = 0, 0  # reset position to the top left corner
    max_row = len(chosen_configuration)
    max_column = len(chosen_configuration[0])
    output = []
    print("The robot must perform the following operations:")
    for letter in word:
        for row in range(max_row):
            for column in range(max_column):
                if chosen_configuration[row][column] == letter:
                    find_horizontal(column,current_column) #activate the find horizontal function
                    find_vertical(row,current_row) #activate the find vertical function
                    output.append("p")  
                    #reset the starting position to the current position
                    current_column = column  
                    current_row = row
                    break
            if chosen_configuration[row][column] == letter:
                break
    
    #print out the actual steps
    for step in output:
        print(step, end="")
    print()  