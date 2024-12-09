'''
Task 1:
Write a program that converts a number of seconds into seconds, minutes, and hours.
- Assume all inputs are positive integers, and
- We write all units in plural, regardless of the quantity (e.g. 0 hours, 1 seconds).
'''

"""
This program converts a number of 
seconds into seconds, minutes, and hours
"""

print("TIME ON EARTH")

# Input time in seconds
total_sec = int(input("Input a time in seconds:\n"))

# Calculate hours, minutes, and seconds
sec = total_sec%60
total_min =  total_sec//60
minute = total_min%60
hour = total_min//60

# Display the result
print("\nThe time on Earth is", hour, "hours", minute, "minutes and", sec, "seconds.")