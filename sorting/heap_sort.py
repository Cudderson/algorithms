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


numbers = [7, 8, 3, 0, 9, 6, 5]
print(f"Unsorted Array: {numbers}")

heap_sort(numbers)

print("Sorted Array: ", end='')
print(numbers)

# Heap Sort in Python

####explanation####