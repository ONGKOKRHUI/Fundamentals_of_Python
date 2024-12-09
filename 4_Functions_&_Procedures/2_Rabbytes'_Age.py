'''
Task 2:
Write a program that, on top of the previous options, allows the user to specify a parent/kitten relationship. 

Main menu
The main prompt now has an extra two options:
==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
0. Quit.
==================================
We recommend you create a function for each menu option, and reuse functions you have written (by improving them if need be) if possible.

4. Create a Parental Relationship
This menu allows the user to indicate a parental relationship between two rabbytes, by first inputting the name of the parent, then the name of the kitten.

Input the parent's name:
Anakin
Input the kitten's name:
Luke
If either name does not correspond to an existing rabbit, a rabbit with that name is created, as it would be if that name was provided through option 1 of the menu. See example 1.

You do not need to verify any consistency of the input. In particular, you may suppose that the user and the automated tests will:
- ensure that the number of parents is between 0 and 2.
- a rabbit cannot be their own ancester.
However, make no other assumptions as to how rabbytes reproduce.

5. List Direct Family of a Rabbit
This menu asks the user to enter a name, and then displays its parents and kittens.

Input the rabbit's name:
Anakin
Parents of Anakin:
Kittens of Anakin:
Leia
Luke
If the input name is not a known rabbit, the program prints

That name is not in the database.
Input the rabbit's name:  
until a known name is provided. The parents and kittens are then displayed as above. See example 2.

Assume that the user (and the automated tests) will only pick option 5 if a rabbit has already been created.

Display the names of the parents and the kittens in alphabetical order. You may use Python's built-in sorting utilites.
'''

'''
This program gives users
the choice of creating 
and storing new rabbits and their age
and establish parent kitten relationship
'''


def main():
    # Display menu options to the user
    print('==================================')
    print("Enter your choice:")
    print("1. Create a Rabbit.")
    print("2. Input Age of a Rabbit.")
    print("3. List Rabbytes.")
    print("4. Create a Parental Relationship.")
    print("5. List Direct Family of a Rabbit.")
    print("0. Quit.")
    print("==================================")

    # Get user input for menu choice
    choice = input()

    # Call corresponding function based on user choice
    if choice == '1':
        create_a_rabbit()
    elif choice == '2':
        input_rabbit_age()
    elif choice == '3':
        list_rabbytes()
    elif choice == '4':
        parental_relationship()
    elif choice == '5':
        list_direct_family()
    elif choice == '0':
        quit()  
    else:
        main() 
# Function to create a new rabbit entry
def create_a_rabbit():
    while True:
        # Ask user for the new rabbit's name
        name = input("Input the new rabbit's name:")
        
        # Check if the rabbit's name already exists in the list
        if name in name_list:
            print("\nThat name is already in the database.")  # Inform the user if name exists
        else:
            # Add the new rabbit name to the name list
            name_list.append(name)
            
            # Add a default age value of "Unknown" to the age list
            age_list.append("Unknown")
            
            # Initialize parent and kitten lists for the new rabbit
            parent_list.append([])
            kitten_list.append([])
            
            print()  # Print a blank line for formatting
            main()  # Return to the main menu

# Function to input or update the age of an existing rabbit
def input_rabbit_age():
    # Ask user for the rabbit's name whose age needs to be updated
    name = input("Input the rabbit's name:")
    
    # Check if the rabbit's name exists in the list
    if name in name_list:
        # Ask user for the rabbit's age
        age = input(f"\nInput {name}'s age:")
        
        # Find the index of the rabbit's name in the list
        name_index = name_list.index(name)
        
        # Update the age in the age list at the found index
        age_list[name_index] = age
        
        print()  # Print a blank line for formatting
        main()  # Return to the main menu
    else:
        # Inform the user if the name does not exist
        print("That name is not in the database.")
        input_rabbit_age()  # Prompt again for valid input

# Function to list all rabbits and their ages
def list_rabbytes():
    print("Rabbytes:")
    
    # Loop through all rabbits and print their names and ages
    for i in range(len(name_list)):
        print(name_list[i],'('+age_list[i]+')')
    
    main()  # Return to the main menu

# Function to create a parental relationship between two rabbits
def parental_relationship():
    # Ask user for the parent's name
    parent = input("Input the parent's name:\n")
    
    # If parent does not exist in the list, add it
    if parent not in name_list:
        name_list.append(parent)
        age_list.append("Unknown")
        parent_list.append([])
        kitten_list.append([])
    
    kitten = input("Input the kitten's name:\n")
    
    # If kitten does not exist in the list, add it
    if kitten not in name_list:
        name_list.append(kitten)
        age_list.append("Unknown")
        parent_list.append([])
        kitten_list.append([])
    
    # Find the indices for parent and kitten
    parent_index = name_list.index(parent)
    kitten_index = name_list.index(kitten)
    
    # Add parent to kitten's parent list if less than 2 parents
    if len(parent_list[kitten_index]) < 2:
        parent_list[kitten_index].append(parent)
    
    # Add kitten to parent's kitten list
    kitten_list[parent_index].append(kitten)
    
    main()  # Return to the main menu

# Function to list the direct family members of a rabbit
def list_direct_family():
    name = input("Input the rabbit's name:\n")
    
    while True:
        if name in name_list:
            name_index = name_list.index(name)
            print("Parents of", name + ':')
            # Sort and print the list of parents
            parent_list[name_index].sort()
            for i in parent_list[name_index]:
                print(i)
            print("Kittens of", name + ':')
            # Sort and print the list of kittens
            kitten_list[name_index].sort()
            for i in kitten_list[name_index]:
                print(i)
            
            main()
        else:
            print("That name is not in the database.")

parent_list = []
kitten_list = []
name_list = []
age_list = []

main()
