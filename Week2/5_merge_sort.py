"""
Merge Sort

"""

"""
Merge Function
merges to sorted lists A and B
"""

def merge(A,B):
    m, n = len(A), len(B)
    C, i, j= [], 0, 0

    # Case 1 When both lists A and B have elements for comparing
    while i < m and j < n:
        if A[i] < B[j]:
            C.append(A[i])
            i = i + 1
        else:
            C.append(B[j])
            j = j + 1
    
    # Case 2 If list A is over shift all elements of B to C
    while i < m:
        C.append(A[i])
        i = i + 1


    # Case 3 If list B is over shift all elements of A to C
    while j < n:
        C.append(B[j])
        j = j + 1
    return C

"""
Lets implement Merge SOrt function that divides the problem into sub problems
"""

"""
Base Case: if the list contains only one element or no element
Recursively call merge sort the left half of the list
Recursively call merge sort the right half of the list 
Merge two sorted lists Left_Half and Right_Half
"""

def mergeSort(L):
    n = len(L)
    # Base Case: if the list contains only one element or no element
    if n <= 1:
        return L
    left = mergeSort(L[:n//2])
    # Recursively call merge sort the left half of the list
    right = mergeSort(L[n//2:])

    SL = merge(left,right)
    return SL

L = [12,43,23,43,123,11,23,331,44,55,22,44]
print(mergeSort(L))

