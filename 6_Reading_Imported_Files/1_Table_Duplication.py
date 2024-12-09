'''
Task 1:
Write a program that allows a user to display and duplicate tables. At the beginning of the program, some tables have to be read from csv files that you must not modify.

Use the module tabulate to print tables in the expected format.

Do not write into files for any of the tasks.

Main menu
The program prompt of the main menu looks like:

==================================
Enter your choice:
1. List tables.
2. Display table.
3. Duplicate table.
0. Quit.
==================================

If the user inputs 1, 2, 3 or 0, it runs the corresponding menu option.

Assume that the user and the automated tests input a correct choice in the main menu.

We recommend you create a function for each menu option.

1. List tables
This menu option prints a table that lists the tables that currently exist in the program.

  Index    Columns    Rows
-------  ---------  ------
      0          5       6
      1          4       7
      2          3       4
      3          3       6
After the header, there is one row per table, with its index, and the number of columns and rows of that table.

At the beginning of the program, all four tables are shown in the list in the order:

grades.csv,

class_students.csv,

rabbytes_club_students.csv,

rabbytes_data.csv,

which then looks exactly as shown above. This list is updated as tables change. See example 1.

2. Display table
This menu option prints a table given its index. 

The program prints Choose a table index (to display):. The user then selects a table by its index (as listed by menu option 1). See below.

Choose a table index (to display):
1
  Student ID  First Name    Last Name    Grade Code
------------  ------------  -----------  ------------
      798154  Brynhildr     Blakeley     N
      134789  Felix         Li           N
      798951  Paityn        Summers      P
      465120  Turnus        Elliot       C
      963245  Alysia        Jervis       D
      469120  Muhammad      Saad         HD

If an incorrect table index is provided, the program prints Incorrect table index. Try again., and prints Choose a table index (to display): again, until a correct index is provided.  See example 2.

For future menu options (including for Tasks 8 and 9), you will also need to check that the table index is correct, and ask again if need be.

For menu option 2 and future menu options, assume that, when asked to input a table index, the user inputs an integer.

3. Duplicate table
Similar to menu option 2, this menu option repeatedly asks the user to select a table, then creates a copy of that table. The index of the new table is the smallest index that has not previously been assigned to a table.

Choose a table index (to duplicate):
1
'''

'''
This program allows users
to display and duplicate 
tables 
'''

#importing libraries
from tabulate import tabulate  
import copy 

# Main function to display menu for user input
def main():
    print("==================================")
    print("Enter your choice:") 
    print("1. List tables.")  
    print("2. Display table.") 
    print("3. Duplicate table.")
    print("0. Quit.")  
    print("==================================")
    
    choice = int(input())  # Reading user's choice as an integer and call respective functions
    if choice == 1:
        list_tables() 
    elif choice == 2:
        display_table() 
    elif choice == 3:
        duplicate_table()  
    elif choice == 0:
        quit() 
    else:
        main()  # If an invalid option is selected, redisplay the menu

# Function to load tables from CSV files and store them in memory
def load_tables():
    table_names = ['grades.csv', 'class_students.csv', 'rabbytes_club_students.csv', 'rabbytes_data.csv']  # List of CSV file names
    for table_index in range(len(table_names)):  # Iterate through each file
        with open(table_names[table_index], 'r') as table:  # Open the CSV file in read mode
            header = table.readline().strip().split(',')  # Read the first line, strip newlines, and split by commas to get headers
            rows = table.readlines()  # Read all remaining rows
            row_list = []
            for row in rows:
                row_list.append(row.split(','))  # Split each row by commas and append to row_list
            tables.append([table_index, header, row_list])  # Append table index, headers, and rows as a list into tables

# Function to list all loaded tables with their index, column count, and row count
def list_tables():
    table_content = []
    for table in tables:
        table_index = table[0]  # Retrieve table index
        column = len(table[1])  # Get the number of columns from the header
        row = len(table[2]) + 1  # Get the number of rows (including header row)
        table_content.append([table_index, column, row])  # Append the table info (index, columns, rows) to table_content
    print(tabulate(table_content, headers=['Index', 'Columns', 'Rows']))  # Print the table info using tabulate for formatting
    main() 

# Function to display a specific table based on user's input of the table index
def display_table():
    print("Choose a table index (to display):")
    table_index = int(input()) 
    if table_index < len(tables) and table_index >= 0:  # Check if the input index is valid
        print(tabulate(tables[table_index][2], headers=tables[table_index][1]))  # Print the table content using tabulate
        main()
    else:
        print("Incorrect table index. Try again.") 
        display_table() 

# Function to duplicate a specific table based on user's input of the table index
def duplicate_table():
    print("Choose a table index (to duplicate):")
    table_index = int(input())
    if table_index < len(tables) and table_index >= 0:  # Check if the input index is valid
        table = copy.deepcopy(tables[table_index])  # Perform a deep copy of the selected table
        table[0] = tables[-1][0] + 1  # Assign a new unique index to the duplicated table (last table index + 1)
        tables.append(table)  # Append the duplicated table to the tables list
        main() 
    else:
        print("Incorrect table index. Try again.") 
        duplicate_table() 

# Initialize an empty list to store all the tables
tables = []

# Load tables from the CSV files
load_tables()

# Start the main program 
main()
