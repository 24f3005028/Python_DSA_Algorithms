"""
Quick Sort
"""

"""
Function 1
    Implement the partition() function
    Args: L-list of integers, low- starting index of the list, high- ending index of the list
    Returns: index of the pivot element after partitioning the list
"""
def partition(L, lower , upper):
    pivot = L[upper]
    i = lower - 1
    for j in range(lower, upper):
        if L[j] <= pivot:
            i += 1
            L[i], L[j] = L[j], L[i]
    
    L[i+1], L[upper] = L[upper], L[i+1]
    return i + 1


"""
Function 2
    Implement the recursive quickSort() function
    Args: L-list of integers, low- starting index of the list, high- ending index of the list
    Returns: sorted list of integers
"""

def quickSort(L, lower , upper):
    if lower < upper:
        pivot = partition(L, lower, upper)
        quickSort(L, lower, pivot - 1)
        quickSort(L,pivot + 1, upper)


L = [12,43,23,43,123,11,23,331,44,55,22,44]
quickSort(L, 0, len(L) - 1)
print(L)