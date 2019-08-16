#! /usr/bin/python3
'''A script to take a string of numbers
and return the smallest, largest, and sum'''

import sys

# Example String - pass into command line
string = "2.2, 1.3, 8.8, 5.5, 3.4, 12.5, 9.9, 2.7, 7.1, 1.1"

def numbers(num_string):
    num_list = num_string.split(', ') # splits by "," and " " to give clean numbers

    # Creates a new list and stores the float versions of the numbers in this list
    num_list_float = []
    for number in num_list:
        num_list_float.append(float(number))

    print(num_list)
    print(num_list_float)

    # Sorts the numbers in the list
    num_list_float.sort()

    #print(num_list)
    #print(len(num_list))
    print("The smallest number is: " + str(num_list_float[0]))
    print("The largest number is: " + str(num_list_float[len(num_list)-1]))
                                        # num_list_float indexed by the length
                                        # of the list - 1 to give the last number

    # Method 1: While Loop (more complicated)
    n = 0
    total = 0
    while n <= (len(num_list_float)) - 1:
        total = total + num_list_float[n]
        n = n + 1
    #print(total)

    # Method 2: sum() function (simple!)
    print("The total of all numbers in the list is: " + str(sum(num_list_float)))

if __name__ == "__main__":

    numbers(sys.argv[1])
