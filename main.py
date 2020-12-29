# --------------------------
#   Author: Subhashis Suara
#   Student ID: UCSE19012
# --------------------------

import time
import random
import numpy as np
import sortingAlgos as sas

# Mention the array sizes
sizes = [10, 100, 1000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]

# Mention the number of times you want to run each algorithm
times = 5

# Number of places to round off
roundOff = 4

class AvgTimings:
    def __init__(self, size, times, roundOff):
        self.size = size
        self.times = times
        self.roundOff = roundOff
        self.measureAvgTime()

    def measureAvgTime(self):
        self.bubbleSortAvgTime = 0
        self.selectionSortAvgTime = 0
        self.insertionSortAvgTime = 0
        self.mergeSortAvgTime = 0
        self.quickSortAvgTime = 0
        # Measures time for each algorithm
        timesCounter = self.times
        while timesCounter > 0:
            # Creates random array of numbers for given size
            inputArray = []
            for num in range(self.size):
                inputArray.append(random.randint(1, self.size))
            
            # Bubble Sort
            startTime = time.time()
            sas.bubbleSort(inputArray)
            endTime = time.time()
            self.bubbleSortAvgTime = (endTime - startTime)
            
            # Selection Sort
            startTime = time.time()
            sas.selectionSort(inputArray)
            endTime = time.time()
            self.selectionSortAvgTime = (endTime - startTime)

            # Insertion Sort
            startTime = time.time()
            sas.insertionSort(inputArray)
            endTime = time.time()
            self.insertionSortAvgTime = (endTime - startTime)

            # Merge Sort
            startTime = time.time()
            sas.mergeSort(inputArray, 0, self.size - 1)
            endTime = time.time()
            self.mergeSortAvgTime = (endTime - startTime)

            # Quick Sort
            startTime = time.time()
            sas.quickSort(inputArray, 0, self.size - 1)
            endTime = time.time()
            self.quickSortAvgTime = (endTime - startTime)

            timesCounter -= 1
        
        # Calculating Average
        self.bubbleSortAvgTime = round((self.bubbleSortAvgTime / self.times), self.roundOff)
        self.selectionSortAvgTime = round((self.selectionSortAvgTime / self.times), self.roundOff)
        self.insertionSortAvgTime = round((self.insertionSortAvgTime / self.times), self.roundOff)
        self.mergeSortAvgTime = round((self.mergeSortAvgTime / self.times), self.roundOff)
        self.quickSortAvgTime = round((self.quickSortAvgTime / self.times), self.roundOff)
    
    def printAvgTimes(self):
        print('---------------------------------')
        print('Specifications ->')
        print(f'Array Size: {self.size}\nTimes Run: {self.times}\nDecimal Round Off: {self.roundOff}')
        print('---------------------------------')
        print('Average Timings (in seconds) ->')
        print(f'Bubble Sort: {self.bubbleSortAvgTime}')
        print(f'Selection Sort: {self.selectionSortAvgTime}')
        print(f'Insertion Sort: {self.insertionSortAvgTime}')
        print(f'Merge Sort: {self.mergeSortAvgTime}')
        print(f'Quick Sort: {self.quickSortAvgTime}')
        print('---------------------------------')

timings = AvgTimings(5000, times, roundOff)
timings.printAvgTimes()