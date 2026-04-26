"""
Linear Search which takes an array and the element to be searched and returns the index of the element if found else returns -1.
Args:   L: List of elements to be searched.
        v: The element to be searched in the list.
Returns: The index of the element if found else returns False.

"""


def linear_search(L,v):
    for i in range(len(L)):
        # when element is found in the list
        if v == L[i]:
            return i
    #when element isnt found int he list
    return False

L=[12,13,14,15]
v=12
w=16
print(linear_search(L,v))
print(linear_search(L,w))