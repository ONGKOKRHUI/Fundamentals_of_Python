'''
Task 2:
Write a program that, on top of the previous options, offers to format variables to snake_case.

Main menu
The main menu now looks like:

==================================
Enter your choice:
1. Print program.
2. List.
3. Format.
0. Quit.
==================================

3. Format
Upon inputting 3, the program asks you to pick one of the variables, and changes its case to snake_case throughout the whole program. For example, if a variable name is:

RobbieTheRobbotor robbieTheRobbot, then it becomes robbie_the_robbot,

robbie_the_robbot, then it remainsrobbie_the_robbot.

If the variable name input by the user does not exist, the program asks again. This is case-sensitive.
'''

"""
This program allows user to list the variables 
of a Python program and format variables to snake_case
"""

import re
import keyword

# this function finds all the variables in the list
def find_variable(list):
    new_list=[]
    var=[]
    for i in list:
        # split string by white spaces
        string=re.split(r"\s",i)
        for x in string:
            # filter string 
            if x.isalpha() or '_' in x:
                new_list.append(x)
    # loop through all the variable in the list
    for i in range(len(new_list)):
        # check if the variable is a python keyword or not
        if new_list[i] not in keyword.kwlist:
            if new_list[i] not in var:

                var.append(new_list[i])
    return var

# this function format the variable into snake_case
def format_var(var,index):
    # change the uppercase characer into snake_case
    var[index]=re.sub(r'(?<!^)(?=[A-Z])', '_', var[index]).lower()

# this function format the list with the new variable
def format_list(var_choose,list,var,index):
    # loop through list to change the old variable name to new variable name 
    for i in range(len(list)):
        list[i]=re.sub(r'\b'+var_choose+r'\b',var[index],list[i])
    

def main():
    list=[]
    # user input python program
    program=input("Enter the Python program to analyze, line by line. Enter 'end' to finish.\n")
    list.append(program)
    while True:
        program=input('')
        # user continue to input the python program until the word end is input 
        if 'end' in program:
            break
        else:
            list.append(program)
    # user input their choice
    user_input=int(input('='*34 + '\nEnter your choice:\n1. Print program.\n2. List.\n3. Format.\n0. Quit.\n'+'='*34+'\n'))
    # call the function find_variable
    var=find_variable(list)
    # the program will continue looping until user input 0
    while user_input !=0:
        if user_input==1:
            print('Program:')
            # print the python program
            for i in list:
                print(i)
        elif user_input==2:
            var=sorted(var)
            print('Variables:')
            # list out all the variables
            for x in range(len(var)):
                print(var[x])
        
        elif user_input==3:
            # ask user to choose a variable to format
            var_choose=input('Pick a variable:\n')
            # check if the variable is valid
            while var_choose not in var:
                print('This is not a variable name.')
                var_choose=input('Pick a variable:\n')
            # find the index of variable choosen by user in the variable list
            for i in range(len(var)):
                    if var_choose==var[i]:
                        index=i
            # call the format_var function
            format_var(var,index)
            #call the format_list function
            format_list(var_choose, list, var, index)

        user_input=int(input('='*34 + '\nEnter your choice:\n1. Print program.\n2. List.\n3. Format.\n0. Quit.\n'+'='*34+'\n'))
main()
