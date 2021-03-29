# Implement Radix Sort in Python


def counting_sort(array, place):

    n = len(array)

    # The output array elements that will have sorted array
    output = [0] * n

    # Initialize count array as 0
    count = [0] * 10

    # Store count of occurrences in count[] (buckets)
    for i in range(0, n):

        index = array[i] / place

        count[int(index % 10)] += 1

    # Change count[i] so that count[i] now contains actual position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = array[i] / place

        # **********
        output[count[int(index % 10)] - 1] = array[i]

        # By decrementing count[], we can safely place the next value in output while maintaining stability (flattening)
        count[int(index % 10)] -= 1

        i -= 1

    # Copy the output array to array[] so that array now contains sorted numbers
    for i in range(0, len(array)):
        array[i] = output[i]


# Main function to implement radix sort
def radix_sort(array):

    # Get maximum element
    maximum = max(array)

    # Apply counting sort to sort elements based on place value
    place = 1
    while int(maximum / place) > 0:
        counting_sort(array, place)
        place *= 10


numbers = [88, 17, 64, 2, 12, 0, 141, 29, 18, 77]

print(f"Unsorted Array: {numbers}")
radix_sort(numbers)
print(f"Sorted array: {numbers}")


# Radix Sort in Python (base=10, d=10)

# Radix Sort is a non-comparative sorting algorithm that uses counting sort as a sub-routine.

# Walk-through

# Our radix sort algorithm will operate by calling counting_sort() repeatedly, with each call sorting the array by the
# next least-significant-digit, and concluding when the most-significant-digit has been evaluated. (In 429, '4' is the M-S-D)

# Our array is first passed to radix sort, where 'place' and 'maximum' are defined, where 'place' represents the current
# digit to sort-by (1), and 'maximum' represents the greatest value in our array. (highest number)

# In base-10, 'place' can be defined as 1, 10, 100, 1000, etc.

# This algorithm is recursive, and the base-case is handled by radix sort's while loop, which will exit when we've
# evaluated the most-significant-digit for the highest value in the array. (while int(maximum / place) > 0: )
#   - We use (int) to convert numbers < 1 to 0. Without this, the loop would run infinitely.

# 1. Our array is passed to counting_sort() for the first iteration, where multiple variables are defined.
#   - 'n' is set to the length of array
#   - two lists/arrays are generated, 'count' and 'output', which will be filled with 0's. >>> [0,0,0,0,0,0,0,0,0,0]
#       - 'count' will be filled with 10 0's, for there are 10 possible values in base10 (0-9) (buckets)
#       - 'output' will be filled with 'n' 0's, to represent a position for each value in our array.

# 2. Next, a for loop begins, which will iterate over the array (for i in range(0, n)) completely.
#   - 'index' is set to array[i] / place. On the first call to counting_sort(), this operation will not change the value.
#   - 'count[int(index % 10)] += 1' executes, which will increment by 1 the position in count[] == int(index % 10)
#   - Assume the value in the unsorted array is 88. 'index' is set to 88.0, and int(88.0 % 10) == 8. Therefore, count[8]
#     is incremented by 1.
#     When this loop in finished, we have a 2-dimensional array that contains the 'count' of digits for the 'place'
#     we're evaluating. (ex. [1, 1, 2, 0, 1, 0, 0, 2, 2, 1])

# reference for next step at: https://stackoverflow.com/questions/15887784/loop-explanation-in-counting-sort
# 3. Next, we enter a for loop (for i in range(1, 10)) that performs one operation: 'count[i] += count[i - 1]'
#   - The purpose of this loop is to calculate the index where each element belongs.
#   - (ex. [1, 2, 4, 4, 5, 5, 5, 7, 9, 10])
#   - *** come back to this ***

# 4. Next, we build our 'output' array, by iterating over our original array in reverse order.
#   - 'i' is set to 'n' - 1 (0-based indexing)
#   - We enter a while loop (while i >= 0) to traverse our original array backwards
#   - 'index' is set to 'array[i] / place'
#   - We then put the value at 'array[i]' into 'output[]', at the position of 'count[int(index % 10)] - 1'
#       - Assume our 'index' is 77.0
#       - 'count[int(index % 10)] - 1' == 'count[int(7)] - 1' == 'subtract 1 from value at count[7]'
#       - We place 'array[i]' at that position in 'output[]'
#       - 'i' is decremented
# ***** begin here *****

# i = n - 1
# while i >= 0:
#     index = array[i] / place
#
#     output[count[int(index % 10)] - 1] = array[i]
#
#     # By decrementing count[], we can safely place the next value in output while maintaining stability (flattening)
#     count[int(index % 10)] -= 1
#
#     i -= 1
