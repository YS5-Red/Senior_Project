from random import sample 
from time import time
from math import floor


class CPU:
    RAM = 24
    startTime = 0
    # sortList = list()
    def __init__(self, memory, sortList) -> None:
        self.memory = memory
        self.sortList = sortList
        
    def makeArray(self, infection):
        nums = sample(range(0,10000*infection), (9000*infection))
        print(len(nums))
        for x in range(len(nums)):
            # print(x)
            sortList.append(nums[x])

        size = len(sortList)

        # print(sortList)
        self.startTime = time()
        self.quickSort(sortList, 0, size - 1)
        print("Array Sorted!")    

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
    def __init__(self) -> None:
        pass

    def stealRAM(self):
        ram = int(input("How much RAM do you want to use? "))
        return ram



sortList = list()
cpu1 = CPU(10, sortList)
crypto = CryptoJacker()
run  = True
while(run):
    print("Input -1 to stop")
    stolen = crypto.stealRAM()
    if stolen < 0:
        break

    infection = floor((stolen / cpu1.RAM) * 500)
    print(infection)

    cpu1.makeArray(infection)
    time = time() - cpu1.startTime
    formatTime = "{:.2f}".format(time)
    print(f"Exectution Time: {formatTime} sec")

print("Done! Thank you")
