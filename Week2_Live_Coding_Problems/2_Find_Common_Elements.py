"""
Write a Python function findCommonElements(L1, L2) that accepts two integer lists L1 and L2 of same length n and return a list that contains elements that are common to both lists. Write a efficient solution that runs in O(nlogn) or better time.

L1 contains all distinct integers and L2 contains all distinct integers, but there can be many elements common between L1 and L2.
Returned list contains all elements that are common to L1 and L2. The elements in the returned list can be in any order.
For example.

if L1 = [5, 8, 2] and L2 = [6, 8, 1] then, findCommonElements(L1, L2) should return list [8].

if L1 = [3, 7, 2, 9, 5] and L2 = [6, 3, 7, 5, 4] then, findCommonElements(L1, L2) should return list [3, 7, 5].


Do not use Python set built-in function


Sample input

[23, 24, 18, 22, 20, 10, 17, 12, 16, 19, 21, 15, 14, 11, 13]
[23, 22, 33, 24, 31, 21, 20, 26, 30, 29, 25, 27, 28, 34, 32]
Output

[20, 21, 22, 23, 24]
Sample input 2

[3, 7, 2, 9, 5]
[6, 3, 7, 5, 4]
Output

[3, 5, 7]
"""

def findCommonElements(L1, L2):
    L1_sorted = sorted(L1)
    L2_sorted = sorted(L2)
    i, j = 0, 0
    result = []
    while i < len(L1) and j < len(L2):
        if L1_sorted[i] == L2_sorted[j]:
            result.append(L1_sorted[i])
            i +=1
            j +=1
        elif L1_sorted[i] < L2_sorted[j]:
            i+= 1
        else:
            j += 1
    return result


# Test
print(findCommonElements([23,24,18,22,20,10,17,12,16,19,21,15,14,11,13],
                         [23,22,33,24,31,21,20,26,30,29,25,27,28,34,32]))
# [20, 21, 22, 23, 24]


"""
How It Works
After sorting, both lists are in ascending order. Two pointers i and j start at the beginning of each list and advance based on comparisons — no nested loops needed.

L1[i] == L2[j] → common element, add to result, advance both pointers

L1[i] < L2[j] → advance i (L1's value is too small to match)

L1[i] > L2[j] → advance j (L2's value is too small to match)
"""