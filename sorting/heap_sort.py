# Implement Heap Sort in Python


def heapify(array, n, i):

    # Find largest root among root children
    largest = i

    # In a complete binary tree, the left and right children of a node 'i' can be expressed by:
    left = 2 * i + 1
    right = 2 * i + 2

    # check if left child is larger than root parent
    if left < n and array[i] < array[left]:
        largest = left

    # check if right child is less than root parent
    if right < n and array[largest] < array[right]:
        largest = right

    # if root is not largest, swap with largest and continue heapifying
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heap_sort(array):

    n = len(array)

    # Build max heap (n//2 because we need to multiply i by 2 to evaluate the node's children
    # We start at i = n//2 because we need to build the max heap from the bottom-up (children first)
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

# Heap Sort is an in-place, comparison-based sorting algorithm that's based on the binary heap data structure.
# Implementing heap sort requires a binary heap, which is a binary tree where elements are stored such that a parent
# node is greater than the values in its two children nodes. (Max Heap) The heap can be represented as a binary
# tree or an array.

# Pseudocode:
# 1. Build a Max Heap from the input array
# 2. After the array is converted to a max heap, the largest item is stored at the top of the heap.
#       - Replace it with the last item of the heap, followed by reducing the size of the heap by 1.
#       - Heapify the root of the tree.
# 3. Repeat step 2 while size of the heap is greater than 1.
# *** The heapify step can only be applied to a node if its children nodes are heapified. Therefore, heapification
# *** must be performed in the bottom-up order.

# Explanation

# Step 1: Building the max heap

# The first for loop in 'heap_sort()' will complete with the array converted to a max heap. It is built from bottom-up
# It begins by heapifying the 'youngest' nodes that could have children (n//2)

# In heapify, the parent node is compared against its 2 children, determining the largest. (left < n, right < n to prevent index error)

# If the parent is not the largest, (largest != i), then the parent and child are swapped.
# If a swap happens, heapify is called again with the new parent, to confirm that it is indeed the largest child.

# After an iteration with no swaps, i is decremented by 1, to represent a new parent node to heapify.
# Because we're examining every parent node in the for loop, and swapping larger nodes with its lesser root, this loop
# cycle will finish with a max heap, where every parent node is greater than its children.

# Step 2: Swap the root with last item in the heap, decrease heap size by 1, and heapify the root.

# With our max heap, the algorithm moves into heap_sort()'s second for loop, where the array will be properly sorted.

# The loop begins with 'for i in range(n-1, 0, -1)'
# Because we start at index 0, n-1 represents the index for the last element in array.

# array[0] and array[i] are swapped, placing the largest element at the end of the array (sorted position)

# Next, heapify(array, i, 0) is called, to heapify the new root node (find largest element between root and children, place at root)

# Once the largest is found, and we return to the for loop, 'i' decrements by 1, and array[0] and array[i] swap, placing
# the largest element in its final sorted position.

# Because we started with a max heap, the next element to place in sorted position will always be available by
# heapifying the root node.

# The process of heapifying the root node, then swapping it with array[i] will continue until 'i' is decremented to 1.
# ( for i in range(n-1, 0, -1 )

# Once the for loop completes, our array is sorted.

# Time Complexity:
# Building the max heap takes O(n) time, but heap_sort takes O(log n) for n iterations.
# Together, heap sort takes O(n*log n)

# Big O: O(n*log n)

# Space Complexity:
# O(1), no extra space is required to sort.
