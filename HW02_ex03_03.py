#!/usr/bin/env python
# HW02_ex03_03

# Python provides a built-in function called len that returns the length 
# of a string, so the value of len('allen') is 5.

# Write a function named right_justify that takes a string named s as a 
# parameter and prints the string with enough leading spaces so that the
# last letter of the string is in column 70 of the display.

# Example:
# >>> right_justify('allen')
#                                                                  allen
################################################################################
# Write your function below:
def right_justify(x):
    l=len(x)
    space=' '
    print (space*(70-l) + x)
#Body







# Write your function above:
################################################################################
def main():
    """Call your functions within this function."""
    print("Hello World!")
    right_justify("Python")
    right_justify("YOUR_NAME")

if __name__ == "__main__":
    main()
