# Implement Linear Search in Python

numbers = [7, 9, 65, 8, 100, 64, 12]


def linear_search(array, x):
    """
    Implements 'linear search' algorithm to find an element's position in an array
    """

    array_length = len(array)

    for i in range(array_length):

        if array[i] == x:

            return i

    return f"Element {x} not found."


element_to_find = 100
x = linear_search(numbers, element_to_find)
print(f"Position of {element_to_find}:")
print(x)

# Pythonic Linear Search

# We can use the 'in' operator to directly evaluate an array

numbers2 = [40, 7, 87, 11, 2, 1, 300]


def linear_search_pythonic(array, x):
    """
    A Pythonic way to find and return an elements position
    """

    if x in array:

        return array.index(x)

    else:

        return f"Element {x} not found."


element_to_find2 = 11
y = linear_search_pythonic(numbers2, element_to_find2)
print(f"Position of {element_to_find2}:")
print(y)


# Linear Search in Python

# 1. The Linear Search Algorithm looks through an array, either left-to-right or right-to-left, looking for a specific
#    element. If the element is found, the algorithm should return that position's element in the searched-array.

# 2. It starts by iterating over an array, with each iteration checking if the current position's value matches
#    the desired element's value.

# 3. If the elements match, return the position of the matched-element in the array, ( if array[i] == x: return i )

# 4. If the element is not found after iterating over the entire array, return that the element was not found.

# ---------------------

# Linear Search (Pythonic)

# In Python, we have access to the 'in' operator. It is classified as a 'membership' operator, which means it is an
# operator that checks for an element's membership within a list, tuple, string, etc. ( 'not in' also exists )

# The 'in' operator checks for a value's existence, and will return 'True' if the element is found, or 'False' if it
# is not found.

# If 'in' evaluates to 'True' (element found), then we return that element's position within the array, with:
# ( return array.index(x) )

# Summary

# No matter how you implement it, linear search is straight-forward. Look through an array/list, one element at
# a time, and if the element being searched for is located in the array, return its position.

# Time Complexity

# Big-O: O(n)
# Omega: O(1) (In its most efficient execution, linear search could find the desired element on the first iteration.)
