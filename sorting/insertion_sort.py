# Implement Insertion Sort in Python


def insertion_sort(array):
    """ Sorts an array/list using the 'insertion sort algorithm' """

    array_length = len(array)

    for i in range(1, array_length):

        # key measures the value of the current iteration's position
        key = array[i]

        # j is set to one position behind 'array[i]' to begin comparison
        j = i - 1

        print(f"\nj = {j}, i = {i}, key = {key}")
        print(array)

        # while j is at valid array position, and position to left of i is greater than i
        while j >= 0 and key < array[j]:

            # elements out of order, move element from left to right
            array[j+1] = array[j]

            # increment j by -1
            j -= 1

        # breaks out when j runs out of room, or when key value is greater than j-value
        # assign the position ahead of j to the key (array[i])
        array[j+1] = key

    return array


# Array to sort
numbers = [17, 4, 88, 90, 0, 4, 12, 14]

print(f"Unsorted array:\n{numbers}")
sorted_array = insertion_sort(numbers)
print(f"Sorted array:\n{sorted_array}")


# Insertion Sort in Python

# 1. Loop over array, from 1 to the length of the array

# 2. Set key = array[i]

# 3. Set j = i -1

# 4. Check if 'key' value 'array[i]' is less than value at j position in array, array[j]
#       - If it is, move j value up one spot
#               - Increment 'j' by -1
#
#       - If it's not, that means we found where 'key' value should go:
#               - Set the position ahead of 'j' to value of the key

#               - Because 'j' is initially at position [i - 1], if the 'while' loop doesn't trigger, the statement
#                 'array[j+1] = key' will just keep the key value where it is.

#               - Begin next iteration

# 5. On each iteration, i increments by 1, to represent evaluating the next value in 'unsorted' part of array
#       - key is set to the value of the 'i' position in array
#       - j is set to 'i - 1', which will measure one spot behind 'i' in array.

# Summary:

# It is common to think of insertion sort in the same way that humans organize cards for a card game.

# Assuming we're sorting from left to right, and that the first card is sorted already, we will take the next card, and
# determine where it should go in the sorted part of our hand. (the cards to the left)

#   - More specifically, we take the 'next' card and check from right-to-left, one card at a time, until we find the
#     correct place for our card in our hand.

#   - The actual code for this algorithm does this by copying the value to the left into its current position, and
#     continuing to do this until the 'card' we are sorting is greater than 'j', the card to the left.

#   - At this point, the card is placed at 'array[j+1]', the place to the right of the card that is finally less-than
#     the card we're sorting.

# In this way, we are constantly 'inserting' the value/card to sort at its correct spot in the already-sorted portion of
# our array/hand.


# Time Complexity:

# Big-O: O(n^2)
# Omega: O(1)   (pre-sorted list)
