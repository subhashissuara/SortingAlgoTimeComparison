# --------------------------
#   Author: Subhashis Suara
#   Student ID: UCSE19012
# --------------------------

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