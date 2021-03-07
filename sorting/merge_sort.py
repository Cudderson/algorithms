# Implement Merge Sort in Python


def merge_sort(array):
    """Sorts an array using the merge sort algorithm"""

    if len(array) > 1:

        # Defining middle of array
        mid = len(array) // 2

        # Divide array in half
        left = array[:mid]

        right = array[mid:]

        # Sort left half
        merge_sort(left)

        # Sort right half
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        # loop until all values in sub-array accounted for
        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # Due to the loop above, at least one value will be still un-accounted for:
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array


#########

numbers = [9, 7, 5, 8]

print(f"Unsorted Array: {numbers}")

sorted_numbers = merge_sort(numbers)

print(f"Merge-Sorted array: {sorted_numbers}")


# Merge Sort in Python (recursive)

# Merge Sort is a 'divide and conquer' algorithm, where an unsorted input array is recursively divided in half until
# there are 'n' sub-arrays of size 1. (n = len(array)) The sub-arrays are compared and placed into sorted order in a
# 2-element array. The sorted 2-element arrays are then 'merged' into sorted 4-element arrays, and so on, until we merge
# into a sorted array of the initial input size.

# Use sample array = [9, 7, 5, 8]

# 1. The function begins with the input array being 'divided' in half and passed into itself recursively with
#    'merge_sort(left)'.

# 2. The recursive call will continue to trigger until the 'if' statement 'len(array) > 1' is no longer true, at which
#    point we hit 'return array', which effectively returns us to line 23, with array = [9, 7], left = [9], and right = [7].
#    - Note that the function will attempt the 'merge_sort()' recursive calls with the 1-element arrays, but it will
#      fail due to the if statement. Instead, the 'return array' will trigger.

# 3. Next, i, j and k are initialized to 0. 'i' will reference 'left[]', j will reference 'right[]', and k will reference
#    'array[]'.

# 4. The first while loop will determine the smaller value between the two 1-element arrays, and place it at 'array[0]'.
#    - i or j will increment depending on if the value from left[] or right[] was copied into array[k]. k increments as well.

# 5. Now, the second while loops are evaluated (lines 39 & 44) to place the un-used left[] or right[] element(s) into array.
#    - We now have a sorted array of 2 elements.

# 6. At this point, 'return array' triggers again, and we return to line 18 with array = [9, 7, 5, 8], left = [7, 9] and
#    right = [5, 8].
#    - left[] is now sorted.

# 7. Next, 'merge_sort(right)' will trigger and the same process will repeat for right = [5, 8].
#    - Though [5, 8] is already sorted, the algorithm will still perform the same operations is if it were unsorted.
#    - Because it didn't need to be sorted, we return to line 21 with the same values as step 6.

# 8. i, j and k are now re-initialized to 0.
#    - Because are size=2 sub-arrays are now sorted, we can evaluate them linearly as we build the final sorted array of
#    size=4.

# 9. This time around, line 34 will trigger, as right[0] < left[0], effectively placing '5' at array[k] = array[0].
#    j and k increment to signal that we are done with both right[0] and array[0].
#    - Temporarily, array = [5, 7, 5, 8]. We can see tha we are just copying the sub-array's values into their appropriate
#      spot in the final array.

# 10. Our while loop triggers again, as this time our sub-arrays are length = 2. This time through, the algorithm evaluates
#     left[0] and right[1], as i hasn't yet been incremented/evaluated. left[0] = 7 is smaller, and it's placed into array[k],
#     which is array[1] now. i and k are incremented again. i = 1, j = 1, k = 2. (i + j = k)
#     - Notice that the first while loop tries to trigger until all values in the sub-array have been evaluated.

# 11. With i and j still less than 2, the while loop triggers again, this time evaluating left[1] and right[1].
#     - right[1] = 8 is smaller, and it's copied into array[k] = array[2]. j and k increment.

# 12. With j = 2, the first while loop can no longer trigger, and we move to the while loops starting at line 39.
#     - These loops compare i and j to the length of left[] and right[]. If i < len(left), or j < len(right), we know
#       that there exists a value that we haven't yet accounted for, as i and j are incremented with every evaluation of
#       left[] and right[]'s elements.

# 13. Here, line 39 will trigger, as i < 2, and left[] has 2 values. left[i] represents the value we haven't yet used,
#     and it's copied into array[k] = array[3]. i and k increment.

#     - 'array[]' is now sorted

# 14. With both while conditions now being false, we move to the last line, 'return array', which returns our sorted array
#     to line 57, where it was originally called.


# Time Complexity:

# Big-O: O(n*log_n)  (n items iterated log_n times)
