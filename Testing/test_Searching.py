import unittest
import random

from Algorithms.Searching.LinearSearch import LinearSearch
from Algorithms.Searching.BinarySearch import BinarySearch
from Algorithms.Searching.JumpSearch import JumpSearch
from Algorithms.Searching.ExponentialSearch import ExponentialSearch
from Algorithms.Searching.TernarySearch import TernarySearch

class TestSearching(unittest.TestCase):
    
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.arr = []
        for i in range(20):
            self.arr.append(random.randint(-100, 100))
            
        self.arr.sort()    
    
    def test_first_value(self):
        self.assertEqual(LinearSearch.linearSearch(self.arr, self.arr[0]), 0, "test_first_value - Linear Search")
        self.assertEqual(BinarySearch.binarySearch(self.arr, self.arr[0]), 0, "test_first_value - Binary Search")
        self.assertEqual(JumpSearch.jumpSearch(self.arr, self.arr[0]), 0, "test_first_value - Jump Search")
        self.assertEqual(ExponentialSearch.exponentialSearch(self.arr, self.arr[0]), 0, "test_first_value - Exponential Search")
        self.assertEqual(TernarySearch.ternarySearch(self.arr, self.arr[0]), 0, "test_first_value - Ternary Search")
        
    def test_last_value(self):
        self.assertEqual(LinearSearch.linearSearch(self.arr, self.arr[len(self.arr) - 1]), len(self.arr) - 1, "test_last_value - Linear Search")
        self.assertEqual(BinarySearch.binarySearch(self.arr, self.arr[len(self.arr) - 1]), len(self.arr) - 1, "test_last_value - Binary Search")
        self.assertEqual(JumpSearch.jumpSearch(self.arr, self.arr[len(self.arr) - 1]), len(self.arr) - 1, "test_last_value - Jump Search")
        self.assertEqual(ExponentialSearch.exponentialSearch(self.arr, self.arr[len(self.arr) - 1]), len(self.arr) - 1, "test_last_value - Exponential Search")
        self.assertEqual(TernarySearch.ternarySearch(self.arr, self.arr[len(self.arr) - 1]), len(self.arr) - 1, "test_last_value - Ternary Search")
        
    def test_first_third_value(self):
        self.assertEqual(LinearSearch.linearSearch(self.arr, self.arr[len(self.arr) // 3]), len(self.arr) // 3, "test_first_third_value - Linear Search")
        self.assertEqual(BinarySearch.binarySearch(self.arr, self.arr[len(self.arr) // 3]), len(self.arr) // 3, "test_first_third_value - Binary Search")
        self.assertEqual(JumpSearch.jumpSearch(self.arr, self.arr[len(self.arr) // 3]), len(self.arr) // 3, "test_first_third_value - Jump Search")
        self.assertEqual(ExponentialSearch.exponentialSearch(self.arr, self.arr[len(self.arr) // 3]), len(self.arr) // 3, "test_first_third_value - Exponential Search")
        self.assertEqual(TernarySearch.ternarySearch(self.arr, self.arr[len(self.arr) // 3]), len(self.arr) // 3, "test_first_third_value - Ternary Search")
        
    def test_second_third_value(self):
        self.assertEqual(LinearSearch.linearSearch(self.arr, self.arr[2 * len(self.arr) // 3]), 2 * len(self.arr) // 3, "test_second_third_value - Linear Search")
        self.assertEqual(BinarySearch.binarySearch(self.arr, self.arr[2 * len(self.arr) // 3]), 2 * len(self.arr) // 3, "test_second_third_value - Binary Search")
        self.assertEqual(JumpSearch.jumpSearch(self.arr, self.arr[2 * len(self.arr) // 3]), 2 * len(self.arr) // 3, "test_second_third_value - Jump Search")
        self.assertEqual(ExponentialSearch.exponentialSearch(self.arr, self.arr[2 * len(self.arr) // 3]), 2 * len(self.arr) // 3, "test_second_third_value - Exponential Search")
        self.assertEqual(TernarySearch.ternarySearch(self.arr, self.arr[2 * len(self.arr) // 3]), 2 * len(self.arr) // 3, "test_second_third_value - Ternary Search")
        
    def test_not_in_arr_lower(self):
        self.assertEqual(LinearSearch.linearSearch(self.arr, -500), -1, "test_not_in_arr_lower - Linear Search")
        self.assertEqual(BinarySearch.binarySearch(self.arr, -500), -1, "test_not_in_arr_lower - Binary Search")
        self.assertEqual(JumpSearch.jumpSearch(self.arr, -500), -1, "test_not_in_arr_lower - Jump Search")
        self.assertEqual(ExponentialSearch.exponentialSearch(self.arr, -500), -1, "test_not_in_arr_lower - Exponential Search")
        self.assertEqual(TernarySearch.ternarySearch(self.arr, -500), -1, "test_not_in_arr_lower - Ternary Search")
    
    def test_not_in_arr_higher(self):
        self.assertEqual(LinearSearch.linearSearch(self.arr, 500), -1, "test_not_in_arr_higher - Linear Search")
        self.assertEqual(BinarySearch.binarySearch(self.arr, 500), -1, "test_not_in_arr_higher - Binary Search")
        self.assertEqual(JumpSearch.jumpSearch(self.arr, 500), -1, "test_not_in_arr_higher - Jump Search")
        self.assertEqual(ExponentialSearch.exponentialSearch(self.arr, 500), -1, "test_not_in_arr_higher - Exponential Search")
        self.assertEqual(TernarySearch.ternarySearch(self.arr, 500), -1, "test_not_in_arr_higher - Ternary Search")