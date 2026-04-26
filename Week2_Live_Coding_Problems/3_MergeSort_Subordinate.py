"""
The Problem (from the image):

You have a shuffled deck of cards (values 0 to 100,000,000). You must sort it using a hierarchical delegation system that mirrors Merge Sort:

Your job (and every subordinate's job): Split the deck into two halves → give each half to a subordinate → receive sorted halves back → merge them in ascending order → return to your superior.

Base case (2 cards): Sort them yourself and return.

Base case (1 card): Return it as-is.

Task: Write def subordinates(L): that returns a tuple of:

The sorted list

The total number of people involved (including yourself)

Example from image:

text
Input:  [3, 1, 2, 0, 5]
Output: ([0, 1, 2, 3, 5], 5)
(5 people: you + subordinate for + subordinate for + sub for + sub for )
"""

def subordinates(L):
    n = len(L)
    if n == 1:
        return(L,1)
    if n == 2:
        return(sorted(L), 1)
    
    mid = n//2
    left_sorted,  left_count  = subordinates(L[:mid])
    right_sorted, right_count = subordinates(L[mid:])

    # Merge two sorted halves
    merged = []
    i, j = 0, 0
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] <= right_sorted[j]:
            merged.append(left_sorted[i]); i += 1
        else:
            merged.append(right_sorted[j]); j += 1
    merged.extend(left_sorted[i:])
    merged.extend(right_sorted[j:])
    total_people = 1 + left_count + right_count
    return (merged, total_people)

# Test
print(subordinates([3, 1, 2, 0, 5]))
# ([0, 1, 2, 3, 5], 5)