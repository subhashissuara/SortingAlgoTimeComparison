# -----------------------------------------
#   Author: Subhashis Suara
#   Student ID: UCSE19012
#   Program Dependencies:
#       Python >= 3.6
#       Numpy (pip install numpy)
#       Matplotlib(pip install matplotlib)
#       sortingAlgos.py file
# -----------------------------------------

import time
import numpy as np
import matplotlib.pyplot as plt
import sortingAlgos as sas

# Mention the array sizes
# Array Sizes: [10, 100, 1000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
sizes = np.array([10, 100, 1000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000])

# Mention the number of times you want to run each algorithm
times = 10

# Number of places to round off
roundOff = 4

class AvgTimings:
    def __init__(self, sizes, times, roundOff):
        self.sizes = sizes
        self.times = times
        self.roundOff = roundOff
        self.bubbleSortTimings = []
        self.selectionSortTimings = []
        self.insertionSortTimings = []
        self.mergeSortTimings = []
        self.quickSortTimings = []

    def measureAvgTime(self, size):
        self.bubbleSortAvgTime = 0
        self.selectionSortAvgTime = 0
        self.insertionSortAvgTime = 0
        self.mergeSortAvgTime = 0
        self.quickSortAvgTime = 0
        # Measures time for each algorithm
        self.timesCounter = self.times
        while self.timesCounter > 0:
            # Creates random arrays of numbers for given size
            inputArray = np.random.randint(1, size, size = size)
            bubbleSortInputArray = np.array(inputArray)
            selectionSortInputArray = np.array(inputArray)
            insertionSortInputArray = np.array(inputArray)
            mergeSortInputArray = np.array(inputArray)
            quickSortInputArray = np.array(inputArray)

            # Bubble Sort
            startTime = time.time()
            sas.bubbleSort(bubbleSortInputArray)
            endTime = time.time()
            self.bubbleSortAvgTime += (endTime - startTime)
            
            # Selection Sort
            startTime = time.time()
            sas.selectionSort(selectionSortInputArray)
            endTime = time.time()
            self.selectionSortAvgTime += (endTime - startTime)
            
            # Insertion Sort
            startTime = time.time()
            sas.insertionSort(insertionSortInputArray)
            endTime = time.time()
            self.insertionSortAvgTime += (endTime - startTime)
            
            # Merge Sort
            startTime = time.time()
            sas.mergeSort(mergeSortInputArray, 0, size - 1)
            endTime = time.time()
            self.mergeSortAvgTime += (endTime - startTime)
            
            # Quick Sort
            startTime = time.time()
            # ---------------------------------------------------------------------------------------------------------
            # sas.quickSort(quickSortInputArray, 0, size - 1) 
            # NOTE: sas.quickSort() works fine but it hits the maximum recursion limit after array size 1000.
            # Hence, for the purpose of measuring timings of large size arrays I am using np.argsort to run quick sort
            quickSortOutputIndexes = np.argsort(quickSortInputArray, None, 'quicksort', None)
            quickSortOutputIndexArray = np.array(quickSortOutputIndexes)
            tempArray = []
            for index in quickSortOutputIndexArray:
                tempArray.append(quickSortInputArray[index])
            quickSortInputArray = np.array(tempArray)
            # ---------------------------------------------------------------------------------------------------------
            endTime = time.time()
            self.quickSortAvgTime += (endTime - startTime)
            
            self.timesCounter -= 1
        
        # Calculating Average
        self.bubbleSortAvgTime = round((self.bubbleSortAvgTime / self.times), self.roundOff)
        self.selectionSortAvgTime = round((self.selectionSortAvgTime / self.times), self.roundOff)
        self.insertionSortAvgTime = round((self.insertionSortAvgTime / self.times), self.roundOff)
        self.mergeSortAvgTime = round((self.mergeSortAvgTime / self.times), self.roundOff)
        self.quickSortAvgTime = round((self.quickSortAvgTime / self.times), self.roundOff)

        # Adding to lists for graph plotting
        self.bubbleSortTimings.append(self.bubbleSortAvgTime)
        self.selectionSortTimings.append(self.selectionSortAvgTime)
        self.insertionSortTimings.append(self.insertionSortAvgTime)
        self.mergeSortTimings.append(self.mergeSortAvgTime)
        self.quickSortTimings.append(self.quickSortAvgTime)
    
    def AvgTimesText(self, size):
        printText = f"""
---------------------------------
Specifications ->
Array Size: {size}\nTimes Run: {self.times}\nDecimal Round Off: {self.roundOff}
---------------------------------
Average Timings (in seconds) ->
Bubble Sort: {self.bubbleSortAvgTime} secs
Selection Sort: {self.selectionSortAvgTime} secs
Insertion Sort: {self.insertionSortAvgTime} secs
Merge Sort: {self.mergeSortAvgTime} secs
Quick Sort: {self.quickSortAvgTime} secs
---------------------------------
"""
        return printText

    def generateTextOutput(self, outputText):
        with open('./timings.txt', 'w') as writeOutput:
            writeOutput.write(outputText)

    def generateGraph(self):
        sizes = list(self.sizes)

        # Graph Plots
        plt.plot(sizes, self.bubbleSortTimings, label = "Bubble Sort", marker='o')
        plt.plot(sizes, self.selectionSortTimings, label = "Selection Sort", marker='o')
        plt.plot(sizes, self.insertionSortTimings, label = "Insertion Sort", marker='o')
        plt.plot(sizes, self.mergeSortTimings, label = "Merge Sort", marker='o')
        plt.plot(sizes, self.quickSortTimings, label = "Quick Sort", marker='o')

        # Graph Details
        plt.xlabel('Array Sizes')
        plt.ylabel('Time Taken (in seconds)')
        plt.title('Comparison of Execution Time for Sorting Algorithms')
        plt.legend()
        plt.savefig('./graph.png')
        # plt.show()

    def main(self):
        outputText = "AVERAGE TIMINGS OUTPUT\n"
        for size in sizes:
            self.measureAvgTime(int(size))
            # NOTE: Add/Remove below comment to not print/print timings in terminal
            print(self.AvgTimesText(size))
            outputText += self.AvgTimesText(size)
        self.generateGraph()
        self.generateTextOutput(outputText)


if __name__ == "__main__":
    timings = AvgTimings(sizes, times, roundOff)
    timings.main()
