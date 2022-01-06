from BinarySearch import BinarySearch

# Exponential Search algorithm uses the Binary Search algorithm as a part of it, So I'm including Binary Search.

class ExponentialSearch:
    @staticmethod
    def exponentialSearch(arr, x):
        """Given a sorted array, searches for a sub array with size that grows exponentially
           and then using binary search on that sub array instead of the whole array to find an element.

        Args:
            arr ((Comparable) Object Array): A sorted array containing comparable objects.
            x (Wanted Elemenet): An object the can be compared with arr's elements.

        Returns:
            Int: Returns the index of the wanted element. If it's not in the array, returns -1.
            
        Time Complexity:
            Worst-Case: O(Log(n))
        """
        if arr[0] == x:
            return 0
        
        i = 1
        
        while i < len(arr) and arr[i] < x:
            i *= 2
            
        if i >= len(arr):
            return -1
        
        return BinarySearch.binarySearchRecursive(arr, x, i // 2, i)
    
if __name__ == "__main__":
    arr = [1, 4, 7, 8, 9, 12, 23, 450, 6048]
    print(ExponentialSearch.exponentialSearch(arr, 1))
    print(ExponentialSearch.exponentialSearch(arr, 8))
    print(ExponentialSearch.exponentialSearch(arr, 6048))
    print(ExponentialSearch.exponentialSearch(arr, 6050))
    