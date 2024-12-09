'''
Task 3:
This task is similar to Task 2, but:
The username and password must match, and
After 3 unsuccessful tries, the user is asked to confirm that they are not a robot so they can try to log in again.

Write a program that asks the user to enter a valid login. In this task, a valid login is a pair of username/password. 
Each username has a single password associated to it. If, after 3 tries, the user did not provide a correct login, 
the program asks whether they are a robot. If they are not a robot, the user is allowed 3 more tries. If they are a robot, the program terminates.

When asked if they are a robot, the prompt reads "Are you a robot (Y/n)?". If the user inputs "Y" or nothing (i.e. ""), 
then the program terminates. If the user enters "n", they are given 3 more tries to log in. If the user enters anything else, 
the prompt "Are you a robot (Y/n)?" is asked again and the user must answer again.

In this task, you may need to:
- use a while loop inside another while loop,
- use lists of lists, and
- use == to compare two lists.
'''

"""
This program prompts the user
to enter a valid and matching 
username and password
up to three tries before confirming
the user is not a robot
"""

#Lists of valid usernames and passwords
username_list = ["Ava","Leo","Raj","Zoe","Max","Sam","Eli","Mia","Ian","Kim"]
password_list = ["12345","abcde","pass1","qwert","aaaaa","zzzzz","11111","apple","hello","admin"]

username = input("Enter username: ")
password = str(input("Enter password: "))

#Counter for number of tries
tries = 0

#While loop prompts until the valid input or number of tries exceeds the limit
while tries < 3:
    #Check if username and password are valid and matching
    if (username in username_list and password in password_list) and username_list.index(username) == password_list.index(password):
        print("Login successful. Welcome", username, "!")
        break
    else:
        print("Login incorrect. Tries left:", 2 - tries)
        tries += 1
        #Only prompt for input if there are tries left
        if tries < 3:  
            username = input("Enter username: ")
            password = str(input("Enter password: "))
        else: 
            #Confirm if user is a robot after three failed attempts
            robot = input("Are you a robot (Y/n)? ") 
            while True:
                #If user is a robot, end the loop
                if robot == "Y" or robot == "":
                    tries = 3
                    break
                #If user is not a robot, reset the number of tries
                elif robot == "n":
                    tries = 0
                    username = input("Enter username: ")
                    password = str(input("Enter password: "))
                    break
                #Prompt again for invalid input
                else:
                    robot = input("Are you a robot (Y/n)? ")
            