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

        # Copy data into temp arrays left[] and right[]
        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # Check if any element was left
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


# rough explanation, will improve

# The tough part to understand is how the recursive calls in the top of the function work.
# The algorithm will keep cutting the original array into 2 halves until they are of size 1.
# At this point, the merge_sort() function cannot enter the 'if' block (len(array) > 1).
# The 'return' statement will trigger, but instead of returning to our script, our program returns
# to the last place the function was called, which is inside of the function itself.
# Since we return to the function call within the if statement, we don't need to pass the 'if' block anymore; we're already inside.
# The same process will be repeated to the initial 'right' side of the array.

# Now, when we return to the recursive call with the array divided into arrays of size 1, the script moves on to the next code,
# which initializes i, k , and j to 0.

###### need to finish ######
