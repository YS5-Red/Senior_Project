import random
from time import sleep


class CPU:
    # sortList = list()
    def __init__(self, memory, sortList) -> None:
        self.memory = memory
        self.sortList = sortList
        
    def makeArray(self):
        nums = random.sample(range(0,100000001), 7500000)
        print(len(nums))
        for x in range(len(nums)):
            sortList.append(nums[x])

        size = len(sortList)

        # print(sortList)
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


sortList = list()
cpu1 = CPU(10, sortList)

cpu1.makeArray()
