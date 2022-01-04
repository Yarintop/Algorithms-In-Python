class BinarySearch:
    @staticmethod
    def binarySearch(arr, x):
        """Given a sorted array, find element x and return its index using the Binary Search algorithm.

        Args:
            arr ((Comparable) Object Array): A sorted array containing comparable objects.
            x (Wanted Elemenet): An object the can be compared with arr's elements.

        Returns:
            Int: Returns the index of the wanted element. If it's not in the array, returns -1.
        """
        lower = 0
        upper = len(arr) - 1
        while lower <= upper:
            currentIndex = (upper + lower) // 2
            if arr[currentIndex] == x:
                return currentIndex
            elif arr[currentIndex] < x:
                lower = currentIndex + 1
            else:
                upper = currentIndex - 1
        return -1
    
    @staticmethod
    def binarySearchRecursive(arr, x, lower=0, upper=None):
        """Given a sorted array, find element x and return its index using a recursive version of the Binary Search algorithm.

        Args:
            arr ((Comparable) Object Array): A sorted array containing comparable objects.
            x (Wanted Elemenet): An object the can be compared with arr's elements.

        Returns:
            Int: Returns the index of the wanted element. If it's not in the array, returns -1.
        """
        if upper == None:
            upper = len(arr) - 1
        if lower <= upper:
            currentIndex = (upper + lower) // 2
            if arr[currentIndex] == x:
                return currentIndex
            elif arr[currentIndex] < x:
                return BinarySearch.binarySearchRecursive(arr, x, currentIndex + 1, upper)
            else:
                return BinarySearch.binarySearchRecursive(arr, x, lower, currentIndex - 1)
        return -1
    
if __name__ == "__main__":
    arr = [1, 4, 7, 8, 9, 12, 23, 450, 6048]
    print(BinarySearch.binarySearch(arr, 8))
    print(BinarySearch.binarySearchRecursive(arr, 8))