import random
import sys

sys.setrecursionlimit(1000)

class QuickSort:
    @staticmethod
    def partition(arr, start, end):
        pivotIndex = start
        pivot = arr[start]
        
        while start < end:
            while start < len(arr) and arr[start] <= pivot:
                start += 1
                
            while arr[end] > pivot:
                end -= 1
            
            if start < end:
                arr[start], arr[end] = arr[end], arr[start]
                
        arr[end], arr[pivotIndex] = arr[pivotIndex], arr[end]
        
        return end
        
    @staticmethod
    def quickSort(arr, start=0, end=None):
        if end == None:
            end = len(arr) - 1
        
        if start < end:
            
            p = QuickSort.partition(arr, start, end)
            
            QuickSort.quickSort(arr, start, p - 1)
            QuickSort.quickSort(arr, p + 1, end)


if __name__ == "__main__":
    arr = []
    for i in range(10):
        arr.append(random.randint(-20, 20))
    print(arr)
    QuickSort.quickSort(arr)
    print(arr)
