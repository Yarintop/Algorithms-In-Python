
class LinearSearch:
    @staticmethod
    def linearSearch(arr, x):
        """Given a sorted array, find element x and return its index using the Linear Search algorithm.

        Args:
            arr ((Comparable) Object Array): An array containing comparable objects.
            x (Wanted Elemenet): An object the can be compared with arr's elements.

        Returns:
            Int: Returns the index of the wanted element. If it's not in the array, returns -1.
            
        Time Complexity:
            Worst-Case: O(n)
        """
        for i, a in enumerate(arr):
            if a == x:
                return i
        return -1
    
if __name__ == "__main__":
    arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
    print(LinearSearch.linearSearch(arr, 10))
    print(LinearSearch.linearSearch(arr, 110))
    print(LinearSearch.linearSearch(arr, 170))
    print(LinearSearch.linearSearch(arr, 175))
    