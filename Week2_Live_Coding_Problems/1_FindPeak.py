"""
Peak Element in Array
Given an array arr[] where no two adjacent elements are same, find the index of a peak element. An element is considered to be a peak element if it is strictly greater than its adjacent elements. If there are multiple peak elements, return the index of any one of them.

Note: Consider the element before the first element and the element after the last element to be negative infinity.

Examples:

Input: arr[] = [1, 2, 4, 5, 7, 8, 3]
Output: 5
Explanation: arr[5] = 8 is a peak element because arr[4] < arr[5] > arr[6].

Input: arr[] = [10, 20, 15, 2, 23, 90, 80]
Output: 1
Explanation: Element 20 at index 1 is a peak since 10 < 20 > 15. Index 5 (value 90) is also a peak, but returning any one peak index is valid.
"""

def peakElement(arr):
    n = len(arr)

    # if only 1 element
    if n <= 1:
        return 0
    # check for the ends
    if arr[0] > arr[1]:
       return 0
    if arr[n-1] > arr[n-2]:
       return 0
    # binary search will be applied from 1, n-2
    
    low, high = 1, n-2
    while low <= high:
        mid = low + (high - low)//2
        # if element at mid is peak then return mid
        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid-1]:
            return mid
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1 

if __name__ == "__main__":
    arr = [1, 2, 4, 5, 7, 8, 3]
    print(peakElement(arr))



