import unittest
import random

class TernarySearch:
    @staticmethod
    def ternarySearch(arr, x, l=0, r=None):
        """
        This algorithm is similar to Binary Search in that it divides the array.
        But in Ternary Search we're dividing the array to three parts instead of 2.
        Binary Search is generally faster than Ternary Search,
        This happens because of the increase in the number of comparisons in Ternary search.
        In simple words, the reduction in the number of iterations in Ternary search is not able to compensate for the increase in comparisons.

        Args:
            arr ((Comparable) Object Array): A sorted array containing comparable objects.
            x (Wanted Elemenet): An object the can be compared with arr's elements.
            l (int, optional): The left "wall" we searching x between. Defaults to 0.
            r (int, optional): The right "wall" we searching x between. Defaults to len(arr) - 1.

        Returns:
            int: x's index if found, else -1.
            
        Time Complexity:
            Worst-Case: O(Log3(n))
        """
        if r == None:
            r = len(arr) - 1
        if l <= r:
            mid1 = l + (r - l) // 3
            mid2 = mid1 + (r - l) // 3
            
            if arr[mid1] == x:
                return mid1
            
            if arr[mid2] == x:
                return mid2
            
            if arr[mid1] > x:
                return TernarySearch.ternarySearch(arr, x, l, mid1 - 1)
            
            if arr[mid2] < x:
                return TernarySearch.ternarySearch(arr, x, mid2 + 1, r)
            
            return TernarySearch.ternarySearch(arr, x, mid1 + 1, mid2 - 1)
        return -1


        
if __name__ == "__main__":
    arr = [1, 4, 7, 8, 9, 12, 23, 450, 6048]
    
        
        