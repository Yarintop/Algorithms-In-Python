import random

class InsertionSort:
    @staticmethod
    def insertionSort(arr):
        """Sort an array using the Insertion Sort algorithm.

        Args:
            arr ((Comparable) objects array): The array we wish to sort.
        
        Time Complexity:
            Worst-Case: O(n^2).
        """
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                j = i - 1
                while j >= 0 and arr[j] > arr[i]:
                    j -= 1
                temp = arr.pop(i)
                arr.insert(j + 1, temp)


if __name__ == "__main__":
    arr = []
    for i in range(10):
        arr.append(random.randint(-20, 20))
    print(arr)
    InsertionSort.insertionSort(arr)
    print(arr)
