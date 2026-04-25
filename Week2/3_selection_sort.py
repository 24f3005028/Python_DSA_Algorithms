"""
Selection Sort
Args: L: List of elements to be sorted.
Returns: Sorted list in ascending order.
"""

def selection_sort(L):
    n = len(L)
    if n <= 1:
        return L
    for i in range(n):
        minpos = i
        for j in range(i+1,n):
            if L[j]<L[minpos]:
                minpos = j
        L[i] , L[minpos] = L[minpos], L[i]
    
    return L



L=[45,3,29,58,3939,583,454,2,443]
print(selection_sort(L))