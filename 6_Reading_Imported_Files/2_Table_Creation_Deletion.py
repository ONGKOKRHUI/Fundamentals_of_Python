'''
Task 2:
Write a program that, on top of the previous options, allows a user to create and delete a table.

Main menu
The program prompt of the main menu looks like:

==================================
Enter your choice:
1. List tables.
2. Display table.
3. Duplicate table.
4. Create table.
5. Delete table.
0. Quit.
==================================

If the user inputs 1, 2, 3, 4, 5, or 0, it runs the corresponding  menu option.

4. Create table
This menu creates a table from an existing table by selecting some of its columns in a certain order.

It repeatedly asks the user Choose a table index (to create from): until a correct index is input.

It then asks the user Enter the comma-separated indices of the columns to keep:.

Each index must be between 0 and the current number of columns of that table, minus one.

The order of the indices determines the order of the columns of the created table.

The index of the new table is the smallest index that has not previously been assigned to a table.

See example 1.

Assume that the user and test inputs are well-formatted (e.g. 3,1, without spaces) and the set of indices is valid.

5. Delete table
This menu option repeatedly asks the user to select a table by its index (as shown by menu option 1) with Choose a table index (for table deletion):, then deletes the table.

Note that deleting a table does not change the indices of other tables. See example 2.
'''

'''
This program allows users
to display, duplicate,
create and delete 
tables 
'''

#Importing libraries
from tabulate import tabulate  
import copy  

def main():
    #display menu options for user input
    print("==================================")
    print("Enter your choice:") 
    print("1. List tables.")  
    print("2. Display table.")
    print("3. Duplicate table.") 
    print("4. Create table.")
    print("5. Delete table.") 
    print("0. Quit.") 
    print("==================================")
    
    choice = int(input())  # Get user's menu choice
    
    # Call respective function based on user input
    if choice == 1:
        list_tables()
    elif choice == 2:
        display_table()
    elif choice == 3:
        duplicate_table()
    elif choice == 4:
        create_table()
    elif choice == 5:
        delete_table()
    elif choice == 0:
        quit()  
    else:
        main()  # If input is invalid, show the menu

#Store tables from the CSV files into a list
def load_tables():
    table_names = ['grades.csv', 'class_students.csv', 'rabbytes_club_students.csv', 'rabbytes_data.csv']
    
    # For each file in table_names, read the contents and store in the 'tables' list.
    for table_index in range(len(table_names)):
        with open(table_names[table_index], 'r') as table:
            header = table.readline().strip().split(',')  # Read the header row and split by commas.
            rows = table.readlines()  # Read all remaining rows of the table.
            row_list = []
            for row in rows:
                row_list.append(row.split(','))  # Split each row by commas.
            tables.append([table_index, header, row_list])  # Append index, header, and rows to tables list.

# List all available tables with their index, column count, and row count.
def list_tables():
    table_content = []
    for table in tables:
        table_index = table[0]
        column = len(table[1])  # Number of columns is length of the header.
        row = len(table[2]) + 1  # Number of rows including the header.
        table_content.append([table_index, column, row])
    print(tabulate(table_content, headers=['Index', 'Columns', 'Rows']))  #print out the table
    main() 

# Display a specific table by index.
def display_table():
    print("Choose a table index (to display):")
    table_index = int(input())
    
    # Validate the table index before displaying it.
    if table_index_condition(table_index) == True:
        list_index = find_list_index(table_index)  # Find internal list index of the table.
        print(tabulate(tables[list_index][2], headers=tables[list_index][1]))  # Display table contents.
        main()  # Return to the main menu.
    else:
        print("Incorrect table index. Try again.")
        display_table()  # Retry if an invalid index is given.

# Duplicate an existing table.
def duplicate_table():
    print("Choose a table index (to duplicate):")
    table_index = int(input())
    
    # Validate table index before duplicating it.
    if table_index_condition(table_index) == True:
        list_index = find_list_index(table_index)  # Find the index in the tables list.
        table = copy.deepcopy(tables[list_index])  # Deep copy the table 
        
        global index_counter
        table[0] = index_counter  # Assign new index to the duplicated table.
        index_counter += 1  # Increment index counter for future tables.
        tables.append(table)  
        main() 
    else:
        print("Incorrect table index. Try again.")
        duplicate_table()  

# Create a new table by selecting columns from an existing one.
def create_table():
    print('Choose a table index (to create from):')
    table_index = int(input())
    
    # Validate the table index (display index) before creating a new table.
    if table_index_condition(table_index) == True:
        list_index = find_list_index(table_index)  #Find the list index of the table (actual index)
        print("Enter the comma-separated indices of the columns to keep:")
        csi = input().split(',')  # Get selected column indices from the user.
        
        header_list = []  # List for storing headers.
        row_list = []  # List for storing rows 
        
        # Add selected headers from the original table.
        for column in csi:
            header_list.append(tables[list_index][1][int(column)])
        
        # Add selected columns from the original table.
        for row in range(len(tables[list_index][2])):
            current_row = []
            for column in csi:
                current_row.append(tables[list_index][2][row][int(column)])
            row_list.append(current_row)
        
        global index_counter
        new_table_index = index_counter  # Assign new index for the new table.
        index_counter += 1 
        tables.append([new_table_index, header_list, row_list])  # Add the new table to the list.
        main() 
    else:
        print("Incorrect table index. Try again.")
        create_table() 

# Delete a table by its index.
def delete_table():
    print("Choose a table index (for table deletion):")
    table_index = int(input())
    
    # Validate the table index (display index) before deletion.
    if table_index_condition(table_index) == True:
        list_index = find_list_index(table_index)   #Find the list index of the table (actual index)
        tables.pop(list_index)  # Remove the table from the list.
        main() 
    else:
        print("Incorrect table index. Try again.")
        delete_table() 

# Check if the given table index (display index) exists in the list.
def table_index_condition(table_index):
    for table in tables:
        if table_index == table[0]:  # If the table index exists, return True.
            return True
    return False  # If not found, return False.

# Find the internal list index (actual index) for a given table index.
def find_list_index(table_index):
    for list_index in range(len(tables)):
        if tables[list_index][0] == table_index:  # Find and return the internal list index.
            return list_index

index_counter = 4  # Index counter to assign new indices to tables.
tables = []  # List to store tables in memory.

load_tables()  # Load tables from the CSV files when the program starts.
main()
