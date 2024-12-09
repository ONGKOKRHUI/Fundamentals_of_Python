'''
Task 3:
Task Description
Main menu
The main prompt now has an extra option:

==================================
Enter your choice:
1. Create a Rabbit.
2. Input Age of a Rabbit.
3. List Rabbytes.
4. Create a Parental Relationship.
5. List Direct Family of a Rabbit.
6. Find Cousins of a Rabbit.
0. Quit.
==================================

We recommend you create a function for each menu option, and reuse functions you have written (by improving them if need be) if possible.

6. Find Cousins of a Rabbit
This menu allows the user to list the cousins of a rabbit. A cousin is a kitten of a sibling of a parent.

Input the rabbit's name:
cousin1
Cousins of cousin1:
cousin2
Similar to menu option 5, it asks the user for a name again

That name is not in the database.
Input the rabbit's name:
until it corresponds to one in the database. See example 1.

Display the names of the cousins in alphabetical order. You may use Python's built-in sorting utilites.

A rabbit cannot be its own cousin. Every other rabbit can.
'''

'''
This program gives users
the choice of creating 
and storing new rabbits and their age
and establish parent kitten relationship
and find the cousin
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
    print("6. Find Cousins of a Rabbit.")
    print("0. Quit.")
    print("==================================")
    choice = input()
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
    elif choice == '6':
        find_cousin()
    elif choice == '0':
        quit() 
    else:
        main() 

# Function to create a new rabbit entry
def create_a_rabbit():
    while True:
        name = input("Input the new rabbit's name:")
        if name in name_list:
            print("\nThat name is already in the database.")  
        else:
            name_list.append(name)
            age_list.append("Unknown")
            parent_list.append([])
            kitten_list.append([])
            
            print()  
            main()

# Function to input or update the age of an existing rabbit
def input_rabbit_age():
    name = input("Input the rabbit's name:")
    
    # Check if the rabbit's name exists in the list
    if name in name_list:
        age = input(f"\nInput {name}'s age:")
        name_index = name_list.index(name)
        age_list[name_index] = age
        
        print()
        main()
    else:
        print("That name is not in the database.")
        input_rabbit_age()

# Function to list all rabbits and their ages
def list_rabbytes():
    print("Rabbytes:")
    
    # Loop through all rabbits and print their names and ages
    for i in range(len(name_list)):
        print(name_list[i], '(' + age_list[i] + ')')
    
    main() 

# Function to create a parental relationship between two rabbits
def parental_relationship():
    parent = input("Input the parent's name:\n")

    # If parent does not exist in the list, add it
    if parent not in name_list:
        name_list.append(parent)
        age_list.append("Unknown")
        parent_list.append([])
        kitten_list.append([])
    
    # Ask user for the kitten's name
    kitten = input("Input the kitten's name:\n")
    
    # If kitten does not exist in the list, add it
    if kitten not in name_list:
        name_list.append(kitten)
        age_list.append("Unknown")
        parent_list.append([])
        kitten_list.append([])
    
    parent_index = name_list.index(parent)
    kitten_index = name_list.index(kitten)
    
    # Add parent to kitten's parent list if less than 2 parents
    if len(parent_list[kitten_index]) < 2:
        parent_list[kitten_index].append(parent)
    
    # Add kitten to parent's kitten list
    kitten_list[parent_index].append(kitten)
    
    main() 

# Function to list the direct family members of a rabbit
def list_direct_family():
    name = input("Input the rabbit's name:\n")
    
    while True:
        # Check if the rabbit's name exists in the list
        if name in name_list:
            # Find the index of the rabbit's name in the list
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

# Function to find and list cousins of a rabbit
def find_cousin():
    cousin_list = []
    
    while True:
        name = input("Input the rabbit's name:\n")
        
        # Check if the rabbit's name exists in the list
        if name in name_list:   
            print("Cousins of", name + ":")
            
            name_index = name_list.index(name)
            
            # If the rabbit has parents, find cousins
            if len(parent_list[name_index]) != 0:
                for parent in parent_list[name_index]:
                    parent_index = name_list.index(parent)
                    
                    # If the parent has parents (grandparents of the rabbit), find their other children
                    if len(parent_list[parent_index]) != 0:
                        for grandparent in parent_list[parent_index]:
                            grandparent_index = name_list.index(grandparent)
                            
                            # For each child of the grandparents, find their children (cousins of the rabbit)
                            if len(kitten_list[grandparent_index]) - 1 != 0:
                                for kitten in kitten_list[grandparent_index]:
                                    if kitten != parent:  # Exclude the parent from being its own cousin
                                        kitten_index = name_list.index(kitten)
                                        
                                        # Add the children of the parent's siblings to the cousin list
                                        if len(kitten_list[kitten_index]) != 0:
                                            for grandkitten in kitten_list[kitten_index]:
                                                cousin_list.append(grandkitten)

            else:
                main()  # If no parents found, return to main menu
            
            # Print the list of cousins
            for cousin in cousin_list:
                print(cousin)
            
            main()
        else:
            print("That name is not in the database.")

parent_list = []
kitten_list = []
name_list = []
age_list = []

main()
