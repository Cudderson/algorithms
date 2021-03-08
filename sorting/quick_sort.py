# Implement Quick Sort in Python


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:

        # If the current value we're looking for is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left
        # to the next element
        # We also need to make sure we haven't surpassed the low pointer, since
        # that indicates we have already moved all the elements to their
        # correct side of the pivot.

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
            # exit loop
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


numbers = [3, 8, 9, 15, 7, 6, 2]
print(f"Unsorted Array: {numbers}")

sorted_array = quick_sort(numbers, 0, len(numbers) - 1)
print(f"Sorted Array: {sorted_array}")


# Quick Sort in Python (recursive, in-place)

# Quick Sort is a 'divide and conquer' algorithm that selects a 'pivot' from a given array and partitions the elements
# into 2 sub-arrays, according to whether they are greater or less than hte pivot.
# The sub-arrays are then sorted recursively.

# Assume array = [3, 8, 9, 15, 7, 6, 2] for this example

# describe functions---The quick_sort() function will first partition() the collection and then recursively call itself on the divided parts.

# *** The Quick Sort algorithm takes in as parameters:
#       1. an unsorted array
#       2. 'start' -- describe
#       3. 'end' -- describe

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
#           - Obviously we don't want our 'low' pointer to pass our 'high' pointer.
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

### Need to finish ###