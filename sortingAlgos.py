# --------------------------
#   Author: Subhashis Suara
#   Student ID: UCSE19012
# --------------------------

def bubbleSort(inputArray): 
    size = len(inputArray)
    for i in range(size): 
        for j in range(0, size - i - 1): 
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