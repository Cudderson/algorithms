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
