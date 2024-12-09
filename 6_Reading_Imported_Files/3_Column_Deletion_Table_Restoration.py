'''
Task 3:
Write a program that, on top of the previous options, allows a user to delete a column and restore a table.

Main menu
The program prompt of the main menu looks like:

==================================
Enter your choice:
1. List tables.
2. Display table.
3. Duplicate table.
4. Create table.
5. Delete table.
6. Delete column.
7. Restore table.
0. Quit.
==================================

If the user inputs 1, 2, 3, 4, 5, 6, 7 or 0, it runs the corresponding menu option.

6. Delete column
This menu option allows the user to delete a column from a table.

Similar to other menu options, the program repeatedly prints Choose a table index (for column deletion): until a correct index is input.

Then the program prints Enter the index of the column to delete:.

The user then inputs one column index, between 0 and the current number of columns of that table, minus one.

That column is then deleted, which is for example reflected in menu option 1 and 2.

See example 1.

Assume that the column index is valid.

Deleting a column in a table does not affect any other table.

7. Restore table
This menu option allows a user to restore a table that has been deleted via menu option 5.

It prompts Choose a table index (for restoration): and reads a table index from the user.

If the table index is invalid (either the table exists and has not been deleted, or has never existed), then the program prints Incorrect table index. Try again., and iterates until a valid index has been input.

The deleted table is then restored with the index it had prior to deletion.

Assume that this menu option is only used if a table has been deleted.
'''

'''
This program allows users
to display, duplicate,
create, delete and
restore tables and
delete a column from a table
'''

#importing libraries
from tabulate import tabulate
import copy

# Main menu for user input
def main():
    print("==================================")
    print("Enter your choice:") 
    print("1. List tables.")
    print("2. Display table.")
    print("3. Duplicate table.")
    print("4. Create table.")
    print("5. Delete table.")
    print("6. Delete column.")
    print("7. Restore table.")
    print("0. Quit.")
    print("==================================")
    choice = int(input())
    
    # Menu options directing to respective functions
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
    elif choice == 6:
        delete_column()
    elif choice == 7:
        restore_table()
    elif choice == 0:
        quit()  # Exits the program
    else:
        main()  


# Load predefined CSV tables into the program memory
def load_tables():
    table_names = ['grades.csv','class_students.csv','rabbytes_club_students.csv','rabbytes_data.csv']
    for table_index in range(len(table_names)):
        with open(table_names[table_index],'r') as table:
            header = table.readline().strip().split(',')
            rows = table.readlines()
            row_list = []
            for row in rows:
                row_list.append(row.split(','))
            # Store tables with their index, header, and rows
            tables.append([table_index, header, row_list])

def list_tables():
    # List the available tables with their index, number of columns, and rows
    table_content = []
    for table in tables:
        table_index = table[0]
        column = len(table[1])
        row = len(table[2]) + 1  # Including header
        table_content.append([table_index, column, row])
    print(tabulate(table_content, headers=['Index', 'Columns', 'Rows']))
    main()

def display_table():
    # Display the selected table by index
    print("Choose a table index (to display):")
    table_index = int(input())
    if table_index_condition(table_index):
        list_index = find_list_index(table_index)
        print(tabulate(tables[list_index][2], headers=tables[list_index][1]))
        main()
    else:
        print("Incorrect table index. Try again.")
        display_table()

def duplicate_table():
    # Create a deep copy of the selected table and assign a new index
    print("Choose a table index (to duplicate):")
    table_index = int(input())
    if table_index_condition(table_index):
        list_index = find_list_index(table_index)
        table = copy.deepcopy(tables[list_index])
        global index_counter
        table[0] = index_counter  # Assign new index
        index_counter += 1
        tables.append(table)  # Add duplicate table to tables
        main()
    else:
        print("Incorrect table index. Try again.")
        duplicate_table()

def create_table():
    # Create a new table by selecting specific columns from an existing table
    print('Choose a table index (to create from):')
    table_index = int(input())
    if table_index_condition(table_index):
        list_index = find_list_index(table_index)
        print("Enter the comma-separated indices of the columns to keep:")
        csi = input().split(',')
        header_list = []
        row_list = []
        # Collect selected columns into a new table
        for column in csi:
            header_list.append(tables[list_index][1][int(column)])
        for row in range(len(tables[list_index][2])):
            current_row = []
            for column in csi:
                current_row.append(tables[list_index][2][row][int(column)])
            row_list.append(current_row)
        global index_counter
        new_table_index = index_counter
        index_counter += 1
        # Append the new table with selected columns
        tables.append([new_table_index, header_list, row_list])
        main()
    else:
        print("Incorrect table index. Try again.")
        create_table()

def delete_table():
    # Delete the selected table and store it in deleted_tables for restoration
    print("Choose a table index (for table deletion):")
    table_index = int(input())
    if table_index_condition(table_index):
        list_index = find_list_index(table_index)
        deleted_tables.append(tables[list_index])  # Store the deleted table in another list
        tables.pop(list_index)  # Remove the table from tables
        main()
    else:
        print("Incorrect table index. Try again.")
        delete_table()

def delete_column():
    # Delete a specific column from the selected table
    print("Choose a table index (for column deletion):")
    table_index = int(input())
    if table_index_condition(table_index):
        list_index = find_list_index(table_index)
        print("Enter the index of the column to delete:")
        delete_index = int(input())
        if delete_index < len(tables[list_index][1]):
            tables[list_index][1].pop(delete_index)  # Remove column from header
            # Remove corresponding column data from each row
            for row in range(len(tables[list_index][2])):
                tables[list_index][2][row].pop(delete_index)
        main()
    else:
        print("Incorrect table index. Try again.")
        delete_column()

def restore_table():
    # Restore a previously deleted table by its index
    print("Choose a table index (for restoration):")
    table_index = int(input())
    for deleted_table_index in range(len(deleted_tables)):
        if table_index == deleted_tables[deleted_table_index][0]:
            # Find appropriate position in the current tables list
            for list_index in range(len(tables)):
                if deleted_tables[deleted_table_index][0] < tables[0][0]:
                    tables.insert(0, deleted_tables[deleted_table_index])
                    break
                elif tables[list_index][0] < deleted_tables[deleted_table_index][0] < tables[list_index + 1][0]:
                    tables.insert(list_index + 1, deleted_tables[deleted_table_index])
                    break
                elif deleted_tables[deleted_table_index][0] > tables[-1][0]:
                    tables.append(deleted_tables[deleted_table_index])
                    break
            main()
    print("Incorrect table index. Try again.")
    restore_table()

def table_index_condition(table_index):
    # Check if the input table index exists in the current tables
    for table in tables:
        if table_index == table[0]:
            return True
    return False

def find_list_index(table_index):
    # Find the list index corresponding to the table index
    for list_index in range(len(tables)):
        if tables[list_index][0] == table_index:
            return list_index

# Initialize necessary global variables
deleted_tables = []  # Store deleted tables
index_counter = 4  # Keep track of the next table index
tables = []  # Store all the tables
load_tables()  # Load predefined tables
main() 
