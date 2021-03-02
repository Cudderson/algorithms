# Implement Selection Sort in Python

# Array to search
numbers = [3, 6, 7, 60, 8, 4, 5, 100, 1, 2, 99, 98, 97, 306]


def selection_sort(array):
    """Sorts an array/list using the 'selection sort' algorithm"""

    # iterate over entire array
    for i in range(len(array)):

        # base value to compare
        minimum = i

        # iterate over all array elements that come after the position we're solving for
        for j in range(i+1, len(array)):

            # set minimum to 'j' if j is less than minimum
            if array[minimum] > array[j]:
                minimum = j

        # Swap array elements if a new minimum value was found
        if minimum != i:
            array[i], array[minimum] = array[minimum], array[i]
            print(f"Swapped {array[i]} with {array[minimum]}")
            print(array)
        else:
            break

    return array


print(numbers)
selection_sort(numbers)

# Selection Sort in Python (pseudocode)

# 1. Function 'selection_sort()' accepts one parameter, 'array', which will be our array to sort.

# 2. We first iterate over the array with 'for i in range(len(array))', where i is the current position we're solving for

# 3. We declare variable 'minimum', which represents the current lowest value in array.
#   - 'minimum' is initialized to 'i', which is the starting position for each iteration.

# 4. Using 'for j in range(i+1, len(array))', inside the original for loop, we can now loop over the rest of the array,
#    looking for a lesser value than minimum.
#   - We start the inner-for loop at 'i+1', because it would be pointless to compare 'minimum' to 'i', they are the same.
#   - 'j' represents each value in the array, starting at 'i+1', or, the next value after our starting point.

# 5. If we find a new minimum value, we set minimum equal to 'j'

# 6. After iterating through entire array, we take the 'minimum' value and 'swap' it with 'array[i]', which is the
#    current position in the array we are solving for.

# 7. When the 'swap' condition evaluates to False (minimum != i), our list must be sorted, so we quit and return
#    the sorted array.

# tip - In Python we can modify arrays\lists in-place; we don't need to create a new sub-array.

# (Think of Selection Sort as an algorithm where we 'solve' each position in the array one at a time, by iterating over
#  the rest of the elements in the array, and swapping the starting position with the minimum value found.)

# Time complexity:

# Big-O: O(n^2)
# Omega: O(n^2)

# Theta: O(n^2)
