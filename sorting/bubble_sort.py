# Implement Bubble Sort in Python

# Array to sort
unsorted_array = [7, 4, 1000, 6, 102, 1, 2, 33, 700]

length = len(unsorted_array)


def bubble_sort(array):
    """Sorts an array/list using the 'bubble sort' algorithm"""

    iterations = 0

    # iterate for as many values in array
    for i in range(length):

        # initialize swap to False. If swap isn't changed to true, program breaks
        swap = False

        # iterate for length of array - 1. To prevent index error with 'j+1'
        for j in range(length - iterations - 1):

            # compare adjacent values
            if array[j] > array[j+1]:

                # set swap = True if values need to be swapped
                swap = True
                array[j], array[j+1] = array[j+1], array[j]
                print(f"\nSwapping {array[j]} with {array[j+1]}")
                print(array)

        iterations += 1
        print(f"Iterations completed: {iterations}")

        if not swap:
            break

    return array


print(unsorted_array)

sorted_array = bubble_sort(unsorted_array)
print(f"Sorted Array: {sorted_array}")

# Bubble Sort in Python (pseudocode)

# 1. Function 'bubble_sort()' takes one parameter, 'array', which is our array to sort

#       - We initialize 'iterations = 0'. This variable will increment with each iteration of the array

# 2. Begin with 'for i in range(length)', which will iterate for as many times that 'array' has elements.
#    Even when least efficient, bubble sort will require n-1 iterations, where n is length of the array.

# 3. Inside for loop, we create another for loop, 'for j in range(length - iterations - 1)'

#       - With each iteration of the array, the (n - iterations) position will be the largest element, where n is the
#         length of the array. (first iteration = n - 0, second iteration = n - 1, n - 2,...)

#       - Because each iteration is guaranteed to find the next-highest position in array, we only iterate through the
#         unsorted portion of the array, with 'length - iterations'

#       - We subtract '1' as well, to prevent index error when 'j+1' is evaluated. All elements will still be evaluated.

# 4. If the condition is True (adjecent elements out of order) they are swapped, and the 'swap' boolean is set to 'True'

#       - The purpose of the 'swap' boolean is to catch when an iteration has made no swaps. When this happens, it means
#         that the array is sorted, and we should stop the execution.

# 5. Function returns the sorted array once it has noticed no 'swaps', or when n-1 iterations finish executing.

# Summary

#     - In bubble sort, each iteration is swapping adjacent values when they are out-of-order, or unsorted.
#       Because of this method, each iteration is guaranteed to find the highest unsorted value, and place it in
#       appropriate sorted order. So, with each iteration, we can examine a smaller portion of the array, using
#       'length - iterations'. This isn't necessary, but an optimization to prevent unnecessary iterating.

# Time Complexity

# Big-O: O(n^2)
# Omega: O(n)  (array provided is already sorted)
