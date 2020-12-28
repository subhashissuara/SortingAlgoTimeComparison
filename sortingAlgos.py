# --------------------------
#   Author: Subhashis Suara
#   Student ID: UCSE19012
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

# Unable to resolve index out of range error
# def combine(inputArray, p, q, r):
#     leftArraySize = q - p + 1
#     rightArraySize = r - q
#     leftArray = [None] * (leftArraySize + 1)
#     rightArray = [None] * (rightArraySize + 1)
#     for i in range(leftArraySize):
#         leftArray[i] = inputArray[p + i]
#     for j in range(rightArraySize):
#         rightArray[j] = inputArray[q + j + 1]
#     leftArray[leftArraySize] = math.inf
#     rightArray[rightArraySize] = math.inf
#     i = 0
#     j = 0
#     for k in range(p, r):
#         if (leftArray[i] < rightArray[j]):
#             inputArray[k] = leftArray[i]
#             i += 1
#         else:
#             inputArray[k] = rightArray[j]
#             j += 1
#     print(inputArray, leftArray, rightArray)

# def mergeSort(inputArray, p, r):
#     if (p < r):
#         q = (p + r) // 2
#         mergeSort(inputArray, p, q)
#         mergeSort(inputArray, q + 1, r)
#         combine(inputArray, p, q, r)
    
def mergeSort(inputArray):
    def combine(inputArray, leftArray, rightArray):
        sizeInputArray = len(inputArray)
        leftArray.append(math.inf)
        rightArray.append(math.inf)
        i = 0
        j = 0

        for k in range(sizeInputArray):
            if leftArray[i] < rightArray[j]:
                inputArray[k] = leftArray[i]
                i += 1
            else:
                inputArray[k] = rightArray[j]
                j += 1
            k += 1

    size = len(inputArray)
    if size > 1:
        midPoint = size // 2
        leftArray = inputArray[:midPoint]
        rightArray = inputArray[midPoint:]
        mergeSort(leftArray)
        mergeSort(rightArray)
        combine(inputArray, leftArray, rightArray)