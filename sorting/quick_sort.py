# Implement Quick Sort in Python


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:

        # check right side
        while low <= high and array[high] >= pivot:
            high -= 1

        # check left side
        while low <= high and array[low] <= pivot:
            low += 1

        # We either found a value for both high and low that is out
        # of order, or low is higher than high, in which case we exit the loop.
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # Loop will trigger again
        else:
            # Exit Loop
            break

    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end):
    """Sorts an array using the quick sort algorithm"""

    if start >= end:
        return

    p = partition(array, start, end)

    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

    return array


numbers = [5, 2, 7, 1, 8, 3, 9, 6]
print(f"Unsorted Array: {numbers}")

sorted_array = quick_sort(numbers, 0, len(numbers) - 1)
print(f"Sorted Array: {sorted_array}")


# Quick Sort in Python (recursive, in-place)

# Quick Sort is a 'divide and conquer' algorithm that selects a 'pivot' from a given array and partitions the elements
# into 2 sub-arrays, according to whether they are greater or less than the pivot.
# The sub-arrays are then sorted recursively.

# *** The Quick Sort algorithm takes in as parameters:
#       1. an unsorted array
#       2. 'start' -- beginning of array
#       3. 'end' -- end of array

# *** We also have another function, 'partition()'.
#    - 'The quick_sort()' function will first 'partition()' the array and then recursively call itself
#       on the divided parts.

# 1. We call 'merge_sort()', and to variable 'p' we assign the result of our 'partition()' function, which takes parameters:
#       - an unsorted array
#       - 'start' of the array, which == index[0]
#       - 'end' of the array, which == len(array) - 1

# 2. Once in the partition function, we assign our 'pivot' to be array[start] == array[0]. 'low' is initialized to
#    'start + 1'. 'high' is initialized to 'end'.

# 3. Next, our program enters the first while loop, which will continue to run until our 'low' pointer is higher than
#    our 'high' pointer.

# 4. Now in the while loop, we enter an inner-while loop that checks that both conditions are true:
#       - low <= high
#       - array[high] >= pivot
#           - Obviously we don't want our 'low' pointer to pass our 'high' pointer, or vice versa.
#           - We check if value at array[high] is greater than the pivot value, where we want it to be.
#    If both are true, we decrease 'high' by -1.
#       - Because value at array[high] is in correct place, we don't need to worry about it anymore (high -= 1)

# 5. Eventually the loop will break-out, and another while loop will trigger that does a mirrored operation for the
#    left side of the array.
#       - The loop will increment the 'low' index pointer by +1 until either:
#           - The 'low' pointer crosses paths with the 'high' pointer
#           - array[low] is not less than or equal to the pivot, indicating the element is in the wrong spot.

# *** If the pointers 'low' and 'high' crossed each other, that means that all elements are on the correct
#     side of the pivot.

# *** Notice that we break out of the while loops when either:
#       - value at index 'low' was not less than the pivot.
#       - value at index 'high' was not greater than the pivot.
#       - or, indexes 'low' and 'high' have crossed.
#
# 6. We next enter an if/else statement to take care of the out-of-place elements our while loops found.
#    - If our index pointers crossed, the 'else' statement triggers and we 'break'.
#    - But, if our pointers haven't crossed, then we swap array[low] with array[high] to place values on the correct side
#      of the pivot.

# 7. Assuming the pointer's haven't yet crossed (else: break), the main while loop will trigger again, looking for elements
#    not on the correct side of the pivot.

# 8. At some point though, 'low' and 'high' will represent the same index and meet at a single-element.
#       - Here, we have no use for the current pivot, as all elements have been placed on the correct side of the pivot.
#       - We swap our pivot, 'array[start]' with 'array[high]'
#       - At this point, all values to the left of our original pivot (now at 'array[high]') are less than it, and values
#         to the right are greater, completing the first recursive step.

# 9. When partition is finished, it returns p = 'high', which was swapped with our pivot. 'quick_sort()' is called again,
#    this time with the range of 0 -> p - 1. 'partition()' will be called again therefore, and will do the same process with
#    a sub-array with everything to the left of our original pivot.

# 10. These recursive calls will continue to trigger until 'start >= end', in which case we 'return'

# 11. At this point, the bottom quick_sort() recursive call will trigger, sorting the initial range of 'p + 1 -> end', where
#     'p' is our original pivot.

# 12. The exact same steps will take place, sorting the size-decreasing sub-arrays on the right side of the original pivot.

# 13. When the 'start >= end' base case triggers this time, we have our sorted array.

### Simplified:

# Divide
# The array is divided into sub-parts taking pivot as the partitioning point. The elements smaller than the pivot are
# placed to the left of the pivot and the elements greater than the pivot are placed to the right.

# Conquer
# The left and the right sub-parts are again partitioned using the by selecting pivot elements for them. This can
# be achieved by recursively passing the sub-parts into the algorithm.

# Combine
# This step does not play a significant role in quick sort. The array is already sorted at the end of the conquer step.

# source: https://www.programiz.com/dsa/quick-sort


# Time Complexity:

# Big-O:
#  - worst case: O(n^2) (pivot chosen is smallest or largest element)
#  - best case:  O(n*log n) (pivot is the middle element or near)
#  - average case: O(n*log n)

# Space Complexity: O(log n)
