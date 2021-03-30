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

        # ********** notice how similar this is to line 19
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


numbers = [304, 425, 406, 323, 289, 385]

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
#   - Notice that the last value in 'count' is equal to the length of the array.
# I think we do the 'rolling sum' in count to give an actual position to each of the 'bucket' values. By adding all of the
# buckets together, we are creating index positions for the output array, as the final bucket will always refer to the
# position in output array with the highest value (for place being evaluated)

# 4. Next, we build our 'output' array, by iterating over our original array in reverse order.
#   - 'i' is set to 'n' - 1 (0-based indexing)
#   - We enter a while loop (while i >= 0) to traverse our original array backwards
#   - 'index' is set to 'array[i] / place'
#   - We then put the value 'array[i]' into 'output[]', at the position of 'count[int(index % 10)] - 1'
#       -  breakdown: 'output[count[int(index % 10)] - 1] = array[i]'
#           - index = 385.0
#           - int(index % 10) = 5
#           - output[count[5] - 1] = array[i], and (count[5] == 4)
#           - output[4 - 1] or output[3] = array[i]
#   - Then, 'count[int(index % 10)] -= 1' executes, which will decrement the value at 'count[]' that we just evaluated in 'output[count[int(index % 10)] - 1] = array[i]'
#   - 'i' is decremented to continue looping

# * iteration 2:
#   - index = 289.0
#   - int(index % 10) = 9
#   - output[count[9] - 1] = array[i], and (count[9] == 6)
#   - output[6 - 1] or output[5] = array[i]
# Then, 'count[int(index % 10)] -= 1' executes, which will decrement the value at 'count[]' that we just evaluated in 'output[count[int(index % 10)] - 1] = array[i]'
#   - This way, if the next value examined refers to the same position in 'count[]', it will be place in its own position in 'output[]'
# 'i' decrements

# We use '-1' to preserve 0-based indexing. Because the total at the end of 'count[]' records the total number of values 'n',
# and the max-position in output is 'n - 1'
# We are also stably-sorting these values. As we iterate backwards in this loop, we are ensuring that a value appearing at
# the end of our original array will be placed higher in the output array than another element of the same value.

# After all iterations, our output array is sorted by the current 'place' we're examining: [323, 304, 425, 385, 406, 289]

# From here, the output array is copied to the original array.

# We return to radix_sort(), where 'place' is multiplied by 10, place = 10 now. This is to examine the 'tens' place of
# the values in our array for sorting.

# The same process repeats, of defining an index (array[i] / place), and incrementing a bucket in 'count' with (index % 10).
# Then, the 'rolling sum' step executes, giving context to each bucket as to where the value relating to that bucket should
# be placed in output[].
# Then, we build the output array.
# We iterate over our array backwards, defining an index the same way (array[i] / place), and using that index's 'bucket' value, 'count[int(index % 10)]',
# to determine the position for array[i] in output[]. (Remember, we do '-1' to preserve 0-based indexing)
# We also decrement the bucket value: 'count[int(index % 10)] -= 1' so that another value with the same bucket isn't placed
# at the same spot in the output array. Also, because we're iterating backwards, values with the same bucket will be placed
# appropriately in the output array. (ex. Iterating forwards would place a value in output[], decrement the bucket, and the
# next value relating to that bucket would be placed *before* the first value, therefore disrupting the original order. By
# iterating backwards, we ensure that values maintain stability/order as they appear in the array.)
# Eventually, the base-case will trigger, when maximum / place is not greater than 0. At this point, we know that we have
# examined the most-significant-digit of the largest value in the original array; the array is sorted.

# **clean up explanation**
