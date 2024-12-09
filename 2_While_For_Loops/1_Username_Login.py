'''
Task 1:
Write a program that asks the user to enter a username. A successful login occurs when the user enters one of the valid usernames. The program keeps prompting the user until a valid username is provided.

The usernames are given below. They are case-sensitive.

Usernames
+----+----+----+----+----+----+----+----+----+----+
| Ava| Leo| Raj| Zoe| Max| Sam| Eli| Mia| Ian| Kim|
+----+----+----+----+----+----+----+----+----+----+
'''

"""
This program keeps prompting
until the user enters a valid username
"""

#List of valid usernames
username_list = ["Ava","Leo","Raj","Zoe","Max","Sam","Eli","Mia","Ian","Kim"]

username = input("Enter username: ")

#While loop keeps prompting until a valid username is entered
while username not in username_list:
    print("Login incorrect.")
    username = input("Enter username: ")

    
print("Login successful. Welcome", username,"!")