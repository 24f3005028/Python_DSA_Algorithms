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


"""
Dry Run — How the Recursion Works
For simplicity, let's trace [12, 43, 23, 43] (first 4 elements):

text
mergeSort([12, 43, 23, 43])
├── mergeSort([12, 43])
│   ├── mergeSort([12]) → [12]   ← base case
│   ├── mergeSort([43]) → [43]   ← base case
│   └── merge([12], [43])
│       12 < 43 → C=[12], then leftover [43] → return [12, 43]
│
├── mergeSort([23, 43])
│   ├── mergeSort([23]) → [23]   ← base case
│   ├── mergeSort([43]) → [43]   ← base case
│   └── merge([23], [43])
│       23 < 43 → C=[23], then leftover [43] → return [23, 43]
│
└── merge([12, 43], [23, 43])
    12 < 23 → C=[12]
    43 > 23 → C=[12, 23]
    43 = 43 → C=[12, 23, 43]  (B[j] taken on else)
    leftover A=[43] → C=[12, 23, 43, 43]
    return [12, 23, 43, 43] ✅
How the 3 while Cases in merge() Work
Case	Condition	Purpose
Case 1	Both i < m and j < n	Compare front of both lists, pick smaller
Case 2	Only i < m (B exhausted)	Dump remaining A into C
Case 3	Only j < n (A exhausted)	Dump remaining B into C
Only one of Case 2 or Case 3 ever runs per merge() call — whichever list still has elements left.

Complexity
            Merge Sort	Insertion Sort	Selection Sort
Best Case	O(n log n)	    O(n)	         O(n²)
Worst Case	O(n log n)	    O(n²)	         O(n²)
Space	    O(n) extra	    O(1)	         O(1)
Merge Sort's consistent O(n log n) comes from always splitting in half (log n levels) and doing O(n) work per level during merging.
"""

