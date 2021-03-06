# --------------------------
#   Author: Subhashis Suara
#   Student ID: UCSE19012
#   Sorting algorithms:
#       Bubble Sort
#       Selection Sort
#       Insertion Sort
#       Merge Sort
#       Quick Sort
# --------------------------

import math

def bubbleSort(inputArray): 
    size = len(inputArray)
    for i in range(size): 
        for j in range(size - i - 1): 
            if inputArray[j] > inputArray[j + 1]:
                temp = inputArray[j]
                inputArray[j] = inputArray[j + 1]
                inputArray[j + 1] = temp

def selectionSort(inputArray):
    size = len(inputArray)
    for i in range(size):
        minElemIndex = i
        for j in range(i + 1, size):
            if(inputArray[minElemIndex] > inputArray[j]):
                minElemIndex = j
        temp = inputArray[minElemIndex]
        inputArray[minElemIndex] = inputArray[i]
        inputArray[i] = temp

def insertionSort(inputArray):
    size = len(inputArray)
    for i in range(1, size):
        key = inputArray[i]
        j = i - 1
        while j >= 0 and inputArray[j] > key:
            inputArray[j + 1] = inputArray[j]
            j -= 1
        inputArray[j + 1] = key

def mergeSort(inputArray, p, r):
    def combine(inputArray, p, q, r):
        leftArraySize = q - p + 1
        rightArraySize = r - q
        leftArray = [None] * (leftArraySize + 1)
        rightArray = [None] * (rightArraySize + 1)
        for i in range(leftArraySize):
            leftArray[i] = inputArray[p + i]
        for j in range(rightArraySize):
            rightArray[j] = inputArray[q + j + 1]
        leftArray[leftArraySize] = math.inf
        rightArray[rightArraySize] = math.inf
        i = 0
        j = 0
        for k in range(p, r + 1):
            if (leftArray[i] < rightArray[j]):
                inputArray[k] = leftArray[i]
                i += 1
            else:
                inputArray[k] = rightArray[j]
                j += 1
    
    if (p < r):
        q = (p + r) // 2
        mergeSort(inputArray, p, q)
        mergeSort(inputArray, q + 1, r)
        combine(inputArray, p, q, r)

# Alternate Method using slicing
# def mergeSort(inputArray):
#     def combine(inputArray, leftArray, rightArray):
#         sizeInputArray = len(inputArray)
#         leftArray.append(math.inf)
#         rightArray.append(math.inf)
#         i = 0
#         j = 0

#         for k in range(sizeInputArray):
#             if leftArray[i] < rightArray[j]:
#                 inputArray[k] = leftArray[i]
#                 i += 1
#             else:
#                 inputArray[k] = rightArray[j]
#                 j += 1
#             k += 1

#     size = len(inputArray)
#     if size > 1:
#         midPoint = size // 2
#         leftArray = inputArray[:midPoint]
#         rightArray = inputArray[midPoint:]
#         mergeSort(leftArray)
#         mergeSort(rightArray)
#         combine(inputArray, leftArray, rightArray)

def quickSort(inputArray, p, r):
    def partition(inputArray, p, r):
        pivotElem = inputArray[r]
        i = p - 1

        for j in range(p, r):
            if(inputArray[j] < pivotElem):
                i += 1
                temp = inputArray[i]
                inputArray[i] = inputArray[j]
                inputArray[j] = temp
        
        temp = inputArray[i + 1]
        inputArray[i + 1] = inputArray[r]
        inputArray[r] = temp
        return i + 1

    if(p < r):
        partitionPoint = partition(inputArray, p, r)
        quickSort(inputArray, p, partitionPoint - 1)
        quickSort(inputArray, partitionPoint + 1, r)