#!/bin/env python3
import os
import random
import numpy as np


# Create a list containing 10,000 random integers.  Write a function that
# returns the position(s) in this list which contain the third-largest value
def create_list():
    numbers_list = [random.randint(0, 10000) for i in range(10000)]
    index_of_3rd_largest(numbers_list)

# The function that identifies the *position(s)* of the 3rd-largest value
def index_of_3rd_largest(numbers_list):
    uniq_list = np.unique(numbers_list)  # get unique values in list
    sorted_list2 = sorted(uniq_list, reverse=True)  # sort unique values in list
    print(sorted_list2[:5])
    third_largest = sorted_list2[2]
    print(third_largest)
    third_largest_index = numbers_list.index(third_largest)
    print(f"The index of the third largest value within the list of random integers is: {third_largest_index}.")

    return None


# Main function: initializes the list of 10000 random integers,
# calls the index_of_3rd_largest function, and prints the result to STDOUT
def main():
    create_list()
    pass


if __name__ == "__main__":
    main()
