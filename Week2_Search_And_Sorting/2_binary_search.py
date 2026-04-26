"""
Binary Search 
Args: L list of elements to be searched.
      v The element to be searched in the list.
Returns: The index of the element if found else returns False.
Prerequisite: The list L should be sorted in ascending order.
"""

def binary_search(L,v):
    low=0
    high = len(L) - 1
    while low <= high:
        mid = (low + high)//2
        if v<L[mid]:
            high = mid - 1
        elif v > L[mid]:
            low = mid + 1
        else:
            return mid
    return False


L = [1,3,4,6,9]
v = 3
w = 9
x = 10

print(binary_search(L,v))
print(binary_search(L,w))
print(binary_search(L,x))
