import unittest
import random

class TernarySearch:
    @staticmethod
    def ternarySearch(arr, x, l=0, r=None):
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
    
        
        