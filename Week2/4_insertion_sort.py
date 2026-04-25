"""
Insertion Sort

Compare current and previous element and swap them if necessary in each iteration

"""



def insertionSort(L):
    n = len(L)
    if n <= 1:
        return L
    for i in range(1,n):
        j = i
        while j>0 and L[j]<L[j-1]:
            L[j-1], L[j] = L[j] , L[j-1]
            j = j-1
    return L

L = [1,5,7,3,5,2,89,0]
print(insertionSort(L))