#!/usr/bin/env python3
# Write a function to sort unsigned 16-bit integers
# that is linear complexity, O(n)
# Since python is not strongly typed, you should ensure
# that the integer values are all in the range 0-65535

def linear_sorting(num_list, y):
    counter = [0] * 10
    array_length = len(num_list)

    for i in range(array_length):
        x = (num_list[i] // y) % 10
        counter[x] += 1

    for i in range(1, 10):
        counter[i] += counter[i - 1]

    outputArray = [0] * array_length
    i = array_length - 1
    while i >= 0:
        current_value = num_list[i]
        x = (num_list[i] // y) % 10
        counter[x] -= 1
        newPosition = counter[x]
        outputArray[newPosition] = current_value
        i -= 1

    return outputArray

def sort_16bit_integers(num_list):
    # TODO: sort algorithm
    n = len(num_list)
    max_value = max(num_list)

    if max_value > 65535:
        raise ValueError("An integer within the list is not within the range 0-65535")

    digits = 1
    while max_value > 0:
        max_value /= 10
        digits+=1

    y = 1

    final_list = num_list
    while digits > 0:
        final_list = linear_sorting(final_list, y)
        y *= 10
        digits -= 1

    return final_list




if __name__ == "__main__":
    test_list_1 = [5676, 32, 1, 19, 65000, 0]
    true_sorted_1 = [0, 1, 19, 32, 5676, 65000]
    sorted_list_1 = sort_16bit_integers(test_list_1)
    print(sorted_list_1)
    assert (sorted_list_1 == true_sorted_1)

    test_list_2 = [300, 200, 65536]
    # This should raise a ValueError
    sorted_list_2 = sort_16bit_integers(test_list_2)
