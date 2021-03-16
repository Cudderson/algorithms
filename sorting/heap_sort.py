# Implement Heap Sort in Python


def heapify(array, n, i):

    # Find largest root among root children
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[i] < array[left]:
        largest = left

    if right < n and array[largest] < array[right]:
        largest = right

    # if root is not largest, swap with largest and continue heapifying
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heap_sort(array):

    n = len(array)

    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        # Swap
        array[i], array[0] = array[0], array[i]

        # Heapify root element
        heapify(array, i, 0)


numbers = [10, 9, 11, 3, 4, 5]
print(f"Unsorted Array: {numbers}")

heap_sort(numbers)

print("Sorted Array: ", end='')
print(numbers)

# Heap Sort in Python

# Heap Sort is a comparison-based sorting algorithm that's based on the binary heap data structure.
# Implementing heap sort requires a binary heap, where elements are stored such that a parent node is greater than
# the values in its two children nodes. (Max Heap) The heap can be represented as a binary tree or an array.

# Pseudocode:
# 1. Build a Max Heap from the input array
# 2. After the array is converted to a max heap, the largest item is stored at the top of the heap.
#       - Replace it with the last item of the heap, followed by reducing the size of the heap by 1.
#       - Heapify the root of the tree.
# 3. Repeat step 2 while size of the heap is greater than 1.
# *** The heapify step can only be applied to a node if its children nodes are heapified. Therefore, heapification
# *** must be performed in the bottom-up order.

# Walkthrough for understanding (breakpoint)

# Step 1: Build max heap from input array

# heap_sort() is called with input array 'numbers'
#  n = 6 (array length)
#  i = 3 (n//2)

# The max heap is built through the for loop (for i in range(n//2, -1, -1))
# which says (for i in range(3 up to -1, stepping by -1)

# Note: In a complete tree, the first index of a non-leaf node is given by 'n/2 - 1'. All other nodes after
#       that are leaf nodes; they don't need to be heapified.

# In the loops first iteration, heapify() is called with parameters (array, n=6, i=3)

# Within heapify, some variables are initialized (largest = i, left = 2 * i + 1, right = 2 * i + 2)
#   - largest = 3
#   - left = 7
#   - right = 8

# An 'if' condition is checked for if left < n, and array[i] < array[left]
# left is not less than n, so condition doesn't trigger.

# Another condition checks if right < n, and array[largest] < array[right]
# right is not less than n, so condition doesn't trigger

# A third condition checks if 'largest != i', which again doesn't trigger

# So, nothing happened the first time calling 'heapify()'
# We return to the first for loop in heap_sort() and the loop continues.
#   - heapify() is called again, with i = 2 this time (because i is decremented by 1)

# This time, in heapify(), variables are re-initialized to:
#   largest = 2
#   left = 5
#   right = 6

# The first condition checks if left < n and array[i] < array[left] >>english>> if 5 < 6 and 11 < 5
#   condition doesn't trigger

# Second condition checks if right < n and array[largest] < array[right] >>english>> if 6 < 6 and 11 < [doesnt exist]
#   condition doesn't trigger

# Third condition checks if largest != i
#   condition doesn't trigger

# We return to the for loop in heap_sort, where i is decremented again, now i = 1, and heapify() is called again
# Varibales re-initialized now to:
#   largest = 1
#   left = 3
#   right = 4

# First condition checks if left < n and array[i] < array[left] >>english>> if 3 < 3 and 9 < 3
#   doesn't trigger

# Second condition checks if right < n and array[largest] < array[right] >>english>> if 4 < 6 and 9 < 4
#   doesn't trigger

# Third condition checks if largest != i
#   doesn't trigger

# Back in the for loop, i is decremented to 0 (final for loop iteration), and heapify() is called.
# Variables reinitialized:
# largest = 0
# left = 1
# right = 2

# first condition doesn't trigger

# second condition checks if right < n and array[largest] < array[right] >>english>> if 2 < 6 and 10 < 11
# Finally it's true and the condition triggers:
#   - largest is set to right >>english>> largest = 2
#   - We have found the largest element in the array

###finish###