'''
Task 1:
POV: you are Robbie the robot using a keyboard. What signal do you send your bionic fingers to type the words?
Write a program that asks the user to input a string, and then plans the actions of Robbie the robot so that it can type this string on a keyboard.

The keyboard has the layout below.

abcdefghijklm
nopqrstuvwxyz
Robbie starts at the top left position (a) and can take the following actions:

u - go up
d - go down
l - go left
r - go right
p - press the key
After pressing a key, Robbie stays on that key. This means:

It can immediately press the same key again.

To go to another key, Robbie will start from the last key it moved to.

Furthermore, Robbie will always move horizontally (left/right) before moving vertically (up/down) when moving to a key it needs to press.

Robbie's actions are restricted by the limits of the board:

It cannot take an action that would make it leave the board.

It cannot wrap around the board. 

Any key not on the keyboard cannot be typed.
'''

'''
This program prompts user to
enter a string and outputs the 
steps to type it out on a keyboard
'''


keyboard = ["abcdefghijklm", "nopqrstuvwxyz"]

steps = []

#setting the initial position of the pointer to top left
current_row = 0
current_column = 0

word = input("Enter a string to type: ")


#checking if all characters in the input are letters
if not word.isalpha():
    print("The string cannot be typed out.")
else:
    print("The robot must perform the following operations:")
    for letter in word:
        #setting a condition to break the loop when the character is found later
        found = False
        for row in range (len(keyboard)): #loop through the total number of rows
            for column in range (len(keyboard[0])): #loop through the total number of columns
                if keyboard[row][column]== letter:
                    found = True
                    #calculating horizontal and vertical moves
                    horizontal = column - current_column
                    vertical = row - current_row
                    #relocating the starting position to current position
                    current_row = row
                    current_column = column
                    break
            if found == True:
                break
        
        #appending steps to a list 
        if horizontal >0:
            for right in range(horizontal):
                steps.append("r")
        elif horizontal <0:
            for right in range(abs(horizontal)):
                steps.append("l")
        if vertical <0:
            steps.append("u")
        elif vertical>0:
            steps.append("d")
        steps.append("p")  
    
    #printing the steps from the list
    for step in steps:
        print(step, end = "")
    print()       