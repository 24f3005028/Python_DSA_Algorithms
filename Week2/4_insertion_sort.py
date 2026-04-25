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


"""
Here's a complete dry run of your Insertion Sort code with `L = [1, 5, 7, 3, 5, 2, 89, 0]`.

## How Insertion Sort Works

The algorithm picks each element (starting from index 1) and **bubbles it leftward** using the `while` loop until it reaches its correct position among the already-sorted left portion. Think of it like sorting cards in your hand — you pick one and slide it left until it fits.

***

## Dry Run: `L = [1, 5, 7, 3, 5, 2, 89, 0]`

### Pass i = 1 — Insert 5
- j=1: L=**5** < L=1? ❌ → No swap 
- State: `[1, 5, 7, 3, 5, 2, 89, 0]`

### Pass i = 2 — Insert 7
- j=2: L=**7** < L=5? ❌ → No swap 
- State: `[1, 5, 7, 3, 5, 2, 89, 0]`

### Pass i = 3 — Insert 3
- j=3: L=**3** < L=7? ✅ → Swap → `[1, 5, 3, 7, 5, 2, 89, 0]`, j=2 
- j=2: **3** < L=5? ✅ → Swap → `[1, 3, 5, 7, 5, 2, 89, 0]`, j=1
- j=1: **3** < L=1? ❌ → Stop
- State: `[1, 3, 5, 7, 5, 2, 89, 0]`

### Pass i = 4 — Insert 5
- j=4: L=**5** < L=7? ✅ → Swap → `[1, 3, 5, 5, 7, 2, 89, 0]`, j=3 
- j=3: **5** < L=5? ❌ → Stop (not strictly less)
- State: `[1, 3, 5, 5, 7, 2, 89, 0]`

### Pass i = 5 — Insert 2
- j=5: L=**2** < L=7? ✅ → Swap → `[1, 3, 5, 5, 2, 7, 89, 0]`, j=4 
- j=4: **2** < L=5? ✅ → Swap → `[1, 3, 5, 2, 5, 7, 89, 0]`, j=3
- j=3: **2** < L=5? ✅ → Swap → `[1, 3, 2, 5, 5, 7, 89, 0]`, j=2 
- j=2: **2** < L=3? ✅ → Swap → `[1, 2, 3, 5, 5, 7, 89, 0]`, j=1 
- j=1: **2** < L=1? ❌ → Stop
- State: `[1, 2, 3, 5, 5, 7, 89, 0]`

### Pass i = 6 — Insert 89
- j=6: L=**89** < L=7? ❌ → No swap 
- State: `[1, 2, 3, 5, 5, 7, 89, 0]`

### Pass i = 7 — Insert 0 (most work!)
- j=7: **0** < 89? ✅ → Swap → `[1, 2, 3, 5, 5, 7, 0, 89]`, j=6
- j=6: **0** < 7? ✅ → Swap → `[1, 2, 3, 5, 5, 0, 7, 89]`, j=5
- j=5: **0** < 5? ✅ → Swap → `[1, 2, 3, 5, 0, 5, 7, 89]`, j=4
- j=4: **0** < 5? ✅ → Swap → `[1, 2, 3, 0, 5, 5, 7, 89]`, j=3
- j=3: **0** < 3? ✅ → Swap → `[1, 2, 0, 3, 5, 5, 7, 89]`, j=2
- j=2: **0** < 2? ✅ → Swap → `[1, 0, 2, 3, 5, 5, 7, 89]`, j=1
- j=1: **0** < 1? ✅ → Swap → `[0, 1, 2, 3, 5, 5, 7, 89]`, j=0
- j=0: Stop (j > 0 fails)
- State: `[0, 1, 2, 3, 5, 5, 7, 89]`

***

## Summary Table

| Pass (i) | Element Inserted | Swaps Made | List After Pass |
|---|---|---|---|
| i = 1 | 5 | 0 | `[1, 5, 7, 3, 5, 2, 89, 0]` |
| i = 2 | 7 | 0 | `[1, 5, 7, 3, 5, 2, 89, 0]` |
| i = 3 | 3 | 2 | `[1, 3, 5, 7, 5, 2, 89, 0]` |
| i = 4 | 5 | 1 | `[1, 3, 5, 5, 7, 2, 89, 0]` |
| i = 5 | 2 | 4 | `[1, 2, 3, 5, 5, 7, 89, 0]` |
| i = 6 | 89 | 0 | `[1, 2, 3, 5, 5, 7, 89, 0]` |
| i = 7 | 0 | 7 | `[0, 1, 2, 3, 5, 5, 7, 89]` ✅ |

**Final Output:** `[0, 1, 2, 3, 5, 5, 7, 89]` ✅

***

## Insertion vs Selection Sort — Quick Contrast

| Feature | Insertion Sort | Selection Sort |
|---|---|---|
| Strategy | Shift current element left to its position | Find global min, place at front |
| Best Case | O(n) — already sorted list | O(n²) always |
| Swaps | Many small swaps per pass | Exactly 1 swap per pass |
| Stable? | ✅ Yes (`<` not `<=`) | ❌ No |

A key advantage of your Insertion Sort: if the list were **nearly sorted**, the `while` loop exits early, making it much faster than Selection Sort in practice.
"""