'''
Task 2: 
This task is similar to Task 1, but:
A password must also be entered,
After 3 unsuccessful tries, the program terminates.
Write a program that asks the user to enter a valid username and a valid password. 
A successful login occurs when the user enters one of the correct usernames and one of the correct passwords. 
If, after 3 tries, the user did not provide a correct login, the program terminates.
'''

""" 
This program prompts the user
to enter a valid username and password
up to three tries before it terminates
"""

#Lists of valid usernames and passwords
username_list = ["Ava","Leo","Raj","Zoe","Max","Sam","Eli","Mia","Ian","Kim"]
password_list = ["12345","abcde","pass1","qwert","aaaaa","zzzzz","11111","apple","hello","admin"]


username = input("Enter username: ")
password = str(input("Enter password: "))

#Counter for the number of tries
tries = 0

#While loop prompts until number of tries exceeds limit
while tries < 3:
    if username in username_list and password in password_list:
        print("Login successful. Welcome", username, "!")
        break
    else:
        print("Login incorrect. Tries left:", 2 - tries)
        tries += 1
        #Only prompt for input if there are tries left
        if tries < 3:  
            username = input("Enter username: ")
            password = str(input("Enter password: "))

