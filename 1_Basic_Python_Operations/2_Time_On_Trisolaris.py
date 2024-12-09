'''
Task 2:
Extend your previous program so that it now also converts a time given in seconds 
into seconds, minutes, and hours, where the conversion from one unit to the other 
is defined during the program, rather than being fixed.
'''

"""
This program converts time in seconds 
into seconds, minutes and hours 
using conversion rate input by user
"""


print("TIME ON EARTH")

#Input time in seconds
total_sec = int(input("Input a time in seconds:\n"))

#Calculate hours, minutes, and seconds
sec = total_sec%60
total_min =  total_sec//60
minute = total_min%60
hour = total_min//60

#Display the result
print("\nThe time on Earth is", hour, "hours", minute, "minutes and", sec, "seconds.")



print("\nTIME ON TRISOLARIS")

#Input the rate of conversion from one unit to another
sec_per_min = int(input("Input the number of seconds in a minute on Trisolaris:\n"))
min_per_hour = int(input("Input the number of minutes in an hour on Trisolaris:\n"))

#Calculate the hours, minutes and seconds using the rates inputted
sec = total_sec%sec_per_min
total_min =  total_sec//sec_per_min
minute = total_min%min_per_hour
hour = total_min//min_per_hour

#Display the result
print("\nThe time on Trisolaris is", hour, "hours", minute, "minutes and", sec, "seconds.")