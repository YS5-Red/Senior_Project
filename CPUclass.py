from random import sample 
from time import time, sleep
from math import floor


class CPU:
    RAM = 24
    startTime = 0
    def __init__(self, memory, sortList) -> None:
        self.memory = memory
        self.sortList = sortList
        
    def makeArray(self, infection):
        multiplier = 1 if infection < 1 else infection
        # print(multiplier)
        nums = sample(range(0,10000*multiplier), (9000*multiplier))
        for x in range(len(nums)):
            sortList.append(nums[x])

        size = len(sortList)

        self.startTime = time()
        self.quickSort(sortList, 0, size - 1)
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
        coinsPerSec = self.cryptoRam * 0.05
        self.coinsMined = coinsPerSec * seconds
    
    def printCoins(self):
        print(f"Mined {self.coinsMined} ShiCoins")
        

def Menu():
    print("---Main Menu---\n" +  
          "1. Run Program\n" + 
          "2. Exit Program\n")
    return int(input("Enter an Option: "))


run = True
sortList = list()
cpu1 = CPU(10, sortList)
crypto = CryptoJacker()

cpu1.makeArray(0)

while(run):
    input = Menu()
    if input == 1: 
        stolen = crypto.stealRAM()
        infection = floor((stolen / cpu1.RAM) * 250)
        cpu1.makeArray(infection)
        time = time() - cpu1.startTime
        crypto.mineCoins(time)
        formatTime = "{:.2f}".format(time)
        print(f"Exectution Time: {formatTime} sec")
        crypto.printCoins()
        break

    elif input == 2:
        print("Done! Thank you")
        run = False
        break

    else: 
        print("Please input a valid menu option (1 or 2)")
