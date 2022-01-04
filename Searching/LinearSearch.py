
class LinearSearch:
    @staticmethod
    def linearSearch(arr, x):
        """Given a sorted array, find element x and return its index using the Linear Search algorithm.

        Args:
            arr ((Comparable) Object Array): The array where we search for the index of the wanted element.
            x (Wanted Elemenet): The wanted element.

        Returns:
            Int: Returns the index of the wanted element. If it's not in the array, returns -1.
        """
        for i, a in enumerate(arr):
            if a == x:
                return i
        return -1