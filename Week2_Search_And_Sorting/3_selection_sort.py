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


"""
Here's a complete dry run of your code with `L = [45, 3, 29, 58, 39]` traced iteration by iteration.

## How Selection Sort Works

The algorithm divides the list into a **sorted left portion** and an **unsorted right portion**. In each outer loop pass (`i`), it finds the minimum element from the unsorted portion and swaps it into position `i`. [geeksforgeeks](https://www.geeksforgeeks.org/dsa/selection-sort-algorithm-2/)

***

## Dry Run: `L = [45, 3, 29, 58, 39]`

### Pass i = 0 — Find min in entire list
- `minpos = 0` → L = **45**
- j=1: L=3 < 45 → `minpos = 1` 
- j=2: L=29 < 3? ❌ 
- j=3: L=58 < 3? ❌ 
- j=4: L=39 < 3? ❌
- **Swap L ↔ L** → `[`**3**, 45, 29, 58, 39`]`

### Pass i = 1 — Find min in L[1:]
- `minpos = 1` → L = **45** 
- j=2: L=29 < 45 → `minpos = 2` 
- j=3: L=58 < 29? ❌ 
- j=4: L=39 < 29? ❌ 
- **Swap L ↔ L** → `[3,` **29**, 45, 58, 39`]` 

### Pass i = 2 — Find min in L[2:]
- `minpos = 2` → L = **45** 
- j=3: L=58 < 45? ❌
- j=4: L=39 < 45 → `minpos = 4` 
- **Swap L ↔ L** → `[3, 29,` **39**, 58, 45`]` 

### Pass i = 3 — Find min in L[3:]
- `minpos = 3` → L = **58** 
- j=4: L=45 < 58 → `minpos = 4` 
- **Swap L ↔ L** → `[3, 29, 39,` **45**, 58`]` 

### Pass i = 4 — Only one element left
- `minpos = 4`, no j to scan
- **No swap** → `[3, 29, 39, 45,` **58**`]`

***

## Summary Table

| Pass (i) | List State After Swap | Element Placed |
|---|---|---|
| Start | `[45, 3, 29, 58, 39]` | — |
| i = 0 | `[`**3**, 45, 29, 58, 39`]` | 3 → index 0 |
| i = 1 | `[3,` **29**, 45, 58, 39`]` | 29 → index 1 |
| i = 2 | `[3, 29,` **39**, 58, 45`]` | 39 → index 2 |
| i = 3 | `[3, 29, 39,` **45**, 58`]` | 45 → index 3 |
| i = 4 | `[3, 29, 39, 45,` **58**`]` | 58 → index 4 |

**Final Output:** `[3, 29, 39, 45, 58]` ✅

***

## Key Points About Your Code

- **Time Complexity:** O(n²) — two nested loops always run regardless of input [youtube](https://www.youtube.com/watch?v=EwjnF7rFLns)
- **In-place sorting:** No extra list is created; swaps happen directly on `L` [w3schools](https://www.w3schools.com/dsa/dsa_algo_selectionsort.php)
- **Stable?** No — equal elements may change relative order due to direct swapping
- Your `if n <= 1: return L` is a nice early-exit guard for edge cases [programiz](https://www.programiz.com/dsa/selection-sort)
"""