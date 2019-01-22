import numpy as np
from selectionSort import selectionSort
from bubbleSort import bubbleSort
from insertionSort import insertionSort
arr = np.array([2, 7, 3, 5, 1, 9, 4, 6, 8])
length = len(arr)

# Sorting algorithms
# selectionSort(arr, length)
# bubbleSort(arr, length)

insertionSort(arr, length)
print(arr)