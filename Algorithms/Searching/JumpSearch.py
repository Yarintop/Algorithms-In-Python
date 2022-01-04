import math

class JumpSearch:
    @staticmethod
    def jumpSearch(arr, x, step=None):
        """Given a sorted array, find element x and return its index using the Jump Search algorithm.

        Args:
            arr ((Comparable) Object Array): A sorted array containing comparable objects.
            x (Wanted Elemenet): An object the can be compared with arr's elements.
            step ([type], optional): The number of steps the algorithm "Jumps" (if none is given, then the default value is the sqrt of len(arr)). Defaults to None.

        Returns:
            Int: Returns the index of the wanted element. If it's not in the array, returns -1.
            
        Time Complexity:
            It is between Linear Search (o(n)) and Binary Search (o(log(n)))
            Worst-Case: depends on step, and is optimized at O(sqrt(n)) while step = sqrt(n).
        """
        if step == None:
            step = math.floor(math.sqrt(len(arr)))
        lower = step
        prev = 0
        while arr[min(lower, len(arr) - 1)] < x:
            prev = lower
            lower += step
            if prev >= len(arr):
                return -1

        for i, a in enumerate(arr[prev:lower]):
            if a == x:
                return i + prev
            
        return -1


if __name__ == "__main__":
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    print(JumpSearch.jumpSearch(arr, 55))
