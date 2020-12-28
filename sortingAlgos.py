def bubbleSort(inputArray): 
    size = len(inputArray)
    for i in range(size): 
        for j in range(0, size - i - 1): 
            if inputArray[j] > inputArray[j + 1]:
                temp = inputArray[j]
                inputArray[j] = inputArray[j + 1]
                inputArray[j + 1] = temp