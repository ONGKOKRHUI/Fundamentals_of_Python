'''
Task 1:
Write a program that allows a user to create and store new rabbytes. Each rabbit is identified by a unique name. 
The program also allows the user to enter a rabbit's age.

Main menu
The program prompt of the main menu looks like:
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
0. Quit.
==================================
If the user inputs 1, 2, 3 or 0, it runs the corresponding function. Otherwise, the prompt is simply printed again. See example 1.
We recommend you create a function for each menu option.

1. Create a Rabbit
Upon inputting 1, the program will then print the prompt

Input the new rabbit's name:
If the user enters a new name, the program returns to the menu and prints the main prompt.

Otherwise, the program prints

That name is already in the database.
Input the new rabbit's name:
and repeat this until the user inputs a new name. See example 2.

2. Input Age of a Rabbit
Upon inputting 2, the program will then print the prompt

Input the rabbit's name:
If the user inputs a name (e.g. rabbie) that is already in the database, the program asks for the rabbit's age:

Input the rabbit's name:
rabbie
Input rabbie's age:
2
It then returns to the main menu and prints the main prompt.

If the user inputs a name that does not exist, the program prints

That name is not in the database.
Input the rabbit's name:
until an existing name is provided. See example 3.

We recommend you store the age of a rabbit using a dictionary. See pre-class content.

We assume that:
- the age input is an integer, 
- the user will only pick option 2 if a rabbit has already been created,
- the user can freely set the age of a rabbit, even if it already has one. It will be updated.

3. List Rabbytes
Upon inputting 3, the program will then print

Rabbytes:
rabbie (42)
not_rabbie (Unknown)
if two rabbytes, rabbie and not_rabbie, have been created before, and if rabbie's age (42) has been input, and not_rabbie's age hasn't. See example 4.
'''

'''
This program gives users
the choice of creating 
and storing new rabbits and their age
'''

def main():
    # Display options to user
    print('==================================')
    print("Enter your choice:")
    print("1. Create a Rabbit.")
    print("2. Input Age of a Rabbit.")
    print("3. List Rabbytes.")
    print("0. Quit.")
    print("==================================")
    # Get user input 
    choice = input()
    # Call function based on user choice
    if choice == '1':
        create_a_rabbit()
    elif choice == '2':
        input_rabbit_age()
    elif choice == '3':
        list_rabbytes()
    elif choice == '0':
        quit()  # Exit the program
    else:
        main()  # If input is invalid, display the menu again

# Function to create a new rabbit
def create_a_rabbit():
    while True:
        name = input("Input the new rabbit's name:")
        # Check if the rabbit's name already exists in the dictionary
        if name in rabbit_dict:
            print("\nThat name is already in the database.")  # Inform the user if name exists
        else:
            # Add the rabbit to the dictionary with a default age of "Unknown"
            rabbit_dict[name] = "Unknown"
            print()
            main()

# Function to input or update the age of an existing rabbit
def input_rabbit_age():
    name = input("Input the rabbit's name:")
    # Check if the rabbit's name exists in the dictionary
    if name in rabbit_dict:
        # Ask user for the rabbit's age
        age = input(f"\nInput {name}'s age:")
        # Update the age for the rabbit in the dictionary
        rabbit_dict[name] = age
        print()
        main()
    else:
        print("That name is not in the database.")
        input_rabbit_age()

# Function to list all rabbits and their ages
def list_rabbytes():
    print("Rabbytes:")
    
    # Loop through all rabbits in the dictionary and print their names and ages
    for name, age in rabbit_dict.items():
        print(f"{name} ({age})")
    main()

# Initialize an empty dictionary to store rabbit names and ages
rabbit_dict = {}

main()

