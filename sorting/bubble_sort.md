# Bubble Sort
Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

```python
def bubbleSort(dat):
    arr = dat.copy()
    swapped = False

    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return arr
```

## Reference
1. https://en.wikipedia.org/wiki/Bubble_sort