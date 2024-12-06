import math

# inital function
def binary_search(sorted_table, element):

    index = math.ceil(len(sorted_table) / 2)

    while element != sorted_table[index]:
        if sorted_table[index] > element:
            index = math.ceil(index / 2)
        else:
            index = math.ceil(index + index /2)
    return index

#debugged function
def binary_search(sorted_table, element):
    
    low = 0
    high = len(sorted_table) - 1

    while low <= high:
        
        index = (low + high) // 2
        
        if sorted_table[index] < element:
            low = index + 1
        elif sorted_table[index] > element:
            high = index - 1
        else:
            return index

"""
comment on intial function: 

The function raises an index out of bounds error if searching for the last element of a table with an uneven number of elements, with a length greater than three.
To fix this, lower and upper bounds must be in place and maintianed in order to keep track of the search space and adjust the index accordingly.

""" 