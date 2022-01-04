import random

class BubbleSort:
    @staticmethod
    def bubbleSort(arr):
        """Sort an array using the Bubble Sort algorithm.

        Args:
            arr ((Comparable) objects array): The array we wish to sort.
        
        Time Complexity:
            Worst-Case: O(n*n). Worst case occurs when array is reverse sorted.
        """
        dirty = True
        while dirty:
            dirty = False
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    temp = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = temp
                    dirty = True
    
if __name__ == "__main__":
    arr = []
    for i in range(10):
        arr.append(random.randint(-20, 20))
    print(arr)
    BubbleSort.bubbleSort(arr)
    print(arr)
    