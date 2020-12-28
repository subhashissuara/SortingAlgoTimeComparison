# --------------------------
#   Author: Subhashis Suara
#   Student ID: UCSE19012
# --------------------------

import sortingAlgos as sas

# Testing all the algorithms

inputArray = [5, 4, 3, 2, 1]
n = len(inputArray)

# # Bubble Sort
# sas.bubbleSort(inputArray)
# print('Bubble Sort:')
# for i in range(len(inputArray)):
#     print(inputArray[i], end=" ")

# # Selection Sort
# sas.selectionSort(inputArray)
# print('Selection Sort:')
# for i in range(len(inputArray)):
#     print(inputArray[i], end=" ")

# # Insertion Sort
# sas.insertionSort(inputArray)
# print('Insertion Sort:')
# for i in range(len(inputArray)):
#     print(inputArray[i], end=" ")

# Merge Sort
sas.mergeSort(inputArray, 0, n - 1)
print('Merge Sort:')
for i in range(len(inputArray)):
    print(inputArray[i], end=" ")

# # Quick Sort
# sas.quickSort(inputArray, 0, n - 1)
# print('Quick Sort:')
# for i in range(len(inputArray)):
#     print(inputArray[i], end=" ")