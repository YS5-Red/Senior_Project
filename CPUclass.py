from random import sample 
from time import time, sleep
from math import floor
from copy import deepcopy


class CPU:
    RAM = 24
    startTime = 0
    sortList = list()
    def __init__(self, memory, sortList) -> None:
        self.memory = memory
        self.sortList = deepcopy(sortList)
        
    def makeArray(self, infection):
        multiplier = 1 if infection < 1 else infection
        # print(multiplier)
        nums = sample(range(0,10000*multiplier), (9000*multiplier))
        for x in range(len(nums)):
            self.sortList.append(nums[x])

        size = len(self.sortList)

        self.startTime = time()
        self.quickSort(self.sortList, 0, size - 1)
        # print("Array Sorted!")    

    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])

        (array[i + 1], array[high]) = (array[high], array[i + 1])

        return i + 1

    def quickSort(self, array, low, high):
        # print("Sorting")
        if low < high:
            pi = self.partition(array, low, high)

            self.quickSort(array, low, pi - 1)
            self.quickSort(array, pi + 1, high)


class CryptoJacker:
    cryptoRam = 0
    run = True
    coinsMined = 0
    def __init__(self) -> None:
        pass

    def stealRAM(self):
        self.cryptoRam = input("How much RAM do you want to use? ")
        return int(self.cryptoRam)
    
    def mineCoins(self, seconds):
        coinsPerSec = float(self.cryptoRam) * 0.05
        self.coinsMined += coinsPerSec * seconds
        print(f"Total ShiCoins mined: {self.coinsMined}")    
     

class Detector:
    def __init__(self) -> None:
        pass

    def detect(self, expectedTime, actualTime):
        if actualTime != expectedTime:
            print("\n-------------------------------------------\n" + 
                  "  WARNING: CRYPTOJACKER RUNNING ON SYSTEM\n" + 
                  "-------------------------------------------\n" + 
                  f"Expected Execution Time: {expectedTime}\n" + 
                  f"Actual Execution Time: {actualTime}")

def Menu():
    print("\n------Main Menu------\n" +  
          "1. Run Program\n" + 
          "2. Exit Program\n")
    return int(input("Enter an Option: ") or 0)


run = True
sortList = list()
cpu = CPU(10, sortList)
crypto = CryptoJacker()

cpu.makeArray(0)
expectedTime = time() - cpu.startTime

while(run):
    userInput = Menu()
    if userInput == 1: 
        del cpu
        cpu = CPU(10, sortList)
        detector = Detector()
        stolen = crypto.stealRAM()
        infection = floor((stolen / cpu.RAM) * 250)
        cpu.makeArray(infection)
        totalTime = time() - cpu.startTime
        crypto.mineCoins(totalTime)
        formatTime = "{:.2f}".format(totalTime)
        print(f"Exectution Time: {formatTime} sec")
        detector.detect("{:.2f}".format(expectedTime), formatTime)

    elif userInput == 2:
        print("Done! Thank you")
        run = False

    else: 
        print("Please input a valid menu option (1 or 2)")
