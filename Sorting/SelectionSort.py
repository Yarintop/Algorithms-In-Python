import random

class SelectionSort:
    @staticmethod
    def selectionSort(arr):
        """Sort an array using the Selection Sort algorithm.

        Args:
            arr ((Comparable) objects array): The array we wish to sort.
        
        Time Complexity:
            Worst-Case: O(n^2) as there are two nested loops.
        """
        for i in range(len(arr)):
            temp = arr[i]
            m = min(arr[i:])
            index = arr[i:].index(m) + i
            arr[i] = m
            arr[index] = temp
    
if __name__ == "__main__":
    arr = []
    for i in range(10):
        arr.append(random.randint(-20, 20))
    print(arr)
    SelectionSort.selectionSort(arr)
    print(arr)
    