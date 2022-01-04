import random

class MergeSort:
    @staticmethod
    def mergeSort(arr):
        """Sort an array using the Merge Sort algorithm.

        Args:
            arr ((Comparable) objects array): The array we wish to sort.
        
        Time Complexity:
            Worst-Case: T(n) = 2T(n/2) + θ(n) || θ(nLog(n))
        """
        if len(arr) == 1:
            return arr
        
        n = len(arr)
        
        l = arr[:n // 2]
        r = arr[n // 2:]
        
        MergeSort.mergeSort(l)
        MergeSort.mergeSort(r)
        
        i = j = k = 0
        
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
            
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1
            
            
if __name__ == "__main__":
    arr = []
    for i in range(10):
        arr.append(random.randint(-20, 20))
    print(arr)
    MergeSort.mergeSort(arr)
    print(arr)
    