'''
Task 3:
Write a program that, on top of the previous options, offers to rename variables.

Main menu
The main menu now looks like:

==================================
Enter your choice:
1. Print program.
2. List.
3. Format.
4. Rename.
0. Quit.
==================================

4. Rename
Upon inputting 4, the program asks you to pick one of the variables, then a new name, and then changes the old name to the new name throughout the whole program. 

If the variable name input by the user does not exist, the program asks again. If the new name is already in use, then the program asks again. This is case-sensitive.

Assume that the new names follow either snake_case, camelCase or PascalCase.
'''

"""
This program allows user to list the variables 
of a Python program, format variables to snake_case
and rename the variable.
"""
import re
import keyword

# this function finds the variables in the list
def find_variable(list):
    new_list=[]
    var=[]
    for i in list:
        # split the string by white space
        string=re.split(r"\s",i)
        for x in string:
            # filter string
            if x.isalpha() or '_' in x:
                new_list.append(x)
    #loop through the variable in the list
    for i in range(len(new_list)):
        # check if the variable is a python keyword
        if new_list[i] not in keyword.kwlist:
            if new_list[i] not in var:

                var.append(new_list[i])
    return var

# this function format the variable
def format_var(var,index):
    # format the variable into snake_case
    var[index]=re.sub(r'(?<!^)(?=[A-Z])', '_', var[index]).lower()

# this function format the list with new variable    
def format_list(var_choose,list,var,index):
    # loop through the list to change variable to snake_case
    for i in range(len(list)):
        list[i]=re.sub(r'\b'+var_choose+r'\b',var[index],list[i])

# this function rename the variable
def var_rename(var_pick,new_var_rename,list):
    # loop through the list to rename the variable with new variable name
    for i in range(len(list)):
        list[i]=re.sub(r'\b'+var_pick+r'\b',new_var_rename,list[i])


def main():
    list=[]
    # ask user to input python program
    program=input("Enter the Python program to analyze, line by line. Enter 'end' to finish.\n")
    list.append(program)
    while True:
        program=input('')
        # ask user to input until the word end is input
        if 'end' in program:
            break
        else:
            list.append(program)
    # ask user for their choice
    user_input=int(input('='*34 + '\nEnter your choice:\n1. Print program.\n2. List.\n3. Format.\n4. Rename.\n0. Quit.\n'+'='*34+'\n'))
    # the program will continue to loop until user input 0
    while user_input !=0:
        if user_input==1:
            print('Program:')
            # loop to print the python program
            for i in list:
                print(i)
        elif user_input==2:
            var=sorted(find_variable(list))
            print('Variables:')
            # list out all the variables in the python program
            for x in range(len(var)):
                print(var[x])
        elif user_input==3:
            var=find_variable(list)
            # ask user to pick a variable to format
            var_choose=input('Pick a variable:\n')
            # check the variable choose by user is valid
            while var_choose not in var:
                print('This is not a variable name.')
                var_choose=input('Pick a variable:\n')
            # find the index of variable choosen by user in the variable list 
            for i in range(len(var)):
                    if var_choose==var[i]:
                        index=i
            # call the function format_var
            format_var(var,index)
            # call the function format_list
            format_list(var_choose, list, var, index)
        elif user_input==4:
            var=find_variable(list)
            # ask user to pick a variable to rename
            var_pick=input('Pick a variable:\n')
            # ensure the variable pick is a variable in the list
            while var_pick not in var:
                print('This is not a variable name.')
                var_pick=input('Pick a variable:\n')
            while True:
                found=False
                new_var_name=input('Pick a new variable name:\n')
                # ensure that the new variable name is a existing variable name
                for char in list:
                    if re.findall(r"\b" + new_var_name + r"\b", char):
                        print('This is already a variable name.')
                        found=True
                        break
                if not found:
                    break

            var_rename(var_pick,new_var_name,list)

        user_input=int(input('='*34 + '\nEnter your choice:\n1. Print program.\n2. List.\n3. Format.\n4. Rename.\n0. Quit.\n'+'='*34+'\n'))
main()

