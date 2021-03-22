# Implement Radix Sort in Python
import time


def counting_sort(array, exp1):

    n = len(array)

    # The output array elements that will have sorted array
    output = [0] * n

    # Initialize count array as 0
    count = [0] * 10

    # Store count of occurrences in count[]
    for i in range(0, n):

        index = array[i] / exp1

        count[int(index % 10)] += 1

    # Change count[i] so that count[i] now contains actual position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = array[i] / exp1

        output[count[int(index % 10)] - 1] = array[i]

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
    while maximum / place > 0:
        counting_sort(array, place)
        place *= 10


numbers = [88, 17, 64, 2, 12, 0, 141, 29, 18, 77]

print(f"Unsorted Array: {numbers}")
radix_sort(numbers)
print(f"Sorted array: {numbers}")


# Radix Sort in Python

###finish explanation###
