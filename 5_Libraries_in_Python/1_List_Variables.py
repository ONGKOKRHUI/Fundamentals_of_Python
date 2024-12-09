'''
Task 1:
Write a program that allows a user to list the variables of a Python program. We suppose that each variable follows one of three cases:
snake_case,
camelCase, or
PascalCase (a.k.a. Upper camel case).
The programs provided as input may not make sense or be correct. Ignore that.
Program input
When the program is run, the user first inputs the program. For example:
Enter the Python program to analyze, line by line. Enter 'end' to finish.
a = b + c
end
Main menu
Once the program is input, the main menu is displayed. The program prompt of the main menu looks like:
==================================
Enter your choice:
1. Print program.
2. List.
0. Quit.
==================================
If the user inputs 1, 2 or 0, it runs the corresponding function. Assume no other input is provided.
We recommend you create at least one function for each menu option.
1. Print program
Upon inputting 1, your program will then print the program that was provided in input (without the "end"):
==================================
Enter your choice:
1. Print program.
2. List.
0. Quit.
==================================
1
Program:
a = b + c

The programs provided as input may have indentation and/or extra spaces. They need to appear as provided when printing the program. See example 1.
2. List
Upon inputting 2, your program will list the variables of the input program. They are provided in alphanumerical order. Each variable is listed only once.
==================================
Enter your choice:
1. Print program.
2. List.
0. Quit.
==================================
2
Variables:
a
b
c

Use Python's sorting functions, such as sorted. You will notice that uppercase words will be listed before lowercase words. This is what we want.

1
print(sorted(["robbie", "Robbie"]))
For the purpose of this and the following task, all variable names
1. start with a lowercase or uppercase character,i.e. a-z and A-Z,
2. may only contain lowercase or uppercase character,i.e. a-z and A-Z, and underscores, i.e. _,
3. cannot be a Python keyword,
4. are surrounded by at least one space on either side.

The programs provided may contain Python keywords. These are not variables. You can programmatically obtain a list of the possible keywords using keyword.kwlist. See example below.

12
import keyword
print(keyword.kwlist)
The input programs do not contain string literals, such as "hello".
'''

"""
This program allows user to list
the variables of a Python program
"""
import re
import keyword

# This function finds the variables in the list
def find_variable(list):
    new_list=[]
    var=[]
    for i in list:
        # split the string by white space
        string=re.split(r"\s",i)
        for x in string:
            # filter the string
            if x.isalpha() or '_' in x:
                new_list.append(x)
    for i in range(len(new_list)):
        # check if the string is a python keyword
        if new_list[i] not in keyword.kwlist:
            if new_list[i] not in var:

                var.append(new_list[i])
    return var


def main():
    list=[]
    # user input python program
    program=input("Enter the Python program to analyze, line by line. Enter 'end' to finish.\n")
    list.append(program)
    while True:
        program=input('')
        # user can input the python program until the word end is input
        if 'end' in program:
            break
        else:
            list.append(program)
    # get user choice
    user_input=int(input('='*34 + '\nEnter your choice:\n1. Print program.\n2. List.\n0. Quit.\n'+'='*34+'\n'))
    # call the function find_variable
    var=find_variable(list)
    # user input 0, the program will stop
    while user_input !=0:
        # if user input 1, it will display the python program
        if user_input==1:
            print('Program:')
            for i in list:
                print(i)
        # if user input 2, it will list out all the variables in the python program
        elif user_input==2:
            var=sorted(var)
            print('Variables:')
            for x in range(len(var)):
                print(var[x])
        user_input=int(input('='*34 + '\nEnter your choice:\n1. Print program.\n2. List.\n0. Quit.\n'+'='*34+'\n'))
main()



