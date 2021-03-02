# Implement Binary Search in Python

# Array to search
numbers = [3, 53, 11, 1, 0, 101, 7, 77]


def binary_search(array, x):
    """
    Searches for an element in array and returns its position
    """

    # Array must be sorted to implement binary search
    array = sorted(array)

    low = 0
    high = len(array) - 1

    while low <= high:

        mid = (low + high) // 2

        if array[mid] > x:

            # x is on left side
            # we know mid != the answer, so subtract 1 to stop evaluating it
            high = mid - 1

        elif array[mid] < x:

            # x is on the right side
            # we know mid != the answer, so add 1
            low = mid + 1

        else:
            # array[mid] == x:
            return mid

    return f"Element {x} not found."


num_to_find = 7
x = binary_search(numbers, num_to_find)
print(f"Position of {num_to_find} in array:\n{x}")


# Binary Search in Python (pseudocode)

# Binary search is a searching algorithm that looks for an element in an array and returns its position.

# This is an iterative implementation of binary search, but note that this algorithm can also be executed recursively.

# 1. To implement binary search, our array/list must be sorted. ( array = sorted(array) )
#    - Assume array is sorted in ascending order for this implementation.

# 2. Binary Search iterates over the array, and compares the current middle-value of the array to the value we are
#    searching for on each iteration.
#    - The middle-value is first determined with 'mid = (high + low) // 2'
#    - We use '//' as a floor-division, so that our 'mid' variable represents a whole number

# 3. If the value we're looking for is less than the current middle-value in array ( if array[mid] > x ), we know that
#    our value is contained to the left of our current middle value.

#    - We know that the right side of the array does not contain our value, so we reset 'high' to 'high = mid - 1'.
#    - We also know that middle-value 'mid' is not the value we want either, so we stop evaluating it with 'mid - 1'
#    - The new range we iterate over is now everything to the left of the middle-value.

# 4. If the value we're looking for is greater than the current middle-value in array ( if array[mid] < x ), we know
#    that our value is contained to the right of our current middle value.

#    - We know that the right side of the array does not contain our value, so we reset 'low' to 'low = mid + 1'
#    - Following the same logic as the previous step, we know that our middle-value is not the value we are looking for,
#      so we stop evaluating it, 'mid + 1'
#    - The new range we iterate over is now everything to the right of the middle value.

# 5. On each iteration, notice that the portion of the array we're examining is cut in half, as our function determines
#    which half of the array our value is located, and stops evaluating the other half. Therefore, binary search is
#    logarithmic.

# 6. At some point, if our value is located in the array, the 'else' condition will trigger, which means that our
#    middle-value is equal to the value we're looking for. At this point, we return 'mid', which represents the index
#    position in the array that our value was found.

# Time Complexity
# Big-O: O(log n)
# Omega: O(1)
