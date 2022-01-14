import unittest
import random

from DataStructures.Trees.BinaryTree.BinaryTree import BinaryTree
from DataStructures.Trees.BinarySearchTree.BinarySearchTree import BinarySearchTree
from DataStructures.Trees.AVLTree.AVLTree import AVLTree
from DataStructures.Trees.SegmentTree.SegmentTree import SegmentTree
from DataStructures.Trees.Trie.Trie import Trie

class TestSearching(unittest.TestCase):
    
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.text = """
            According to all known laws
            of aviation,
            
            there is no way a bee
            should be able to fly.

            Its wings are too small to get
            its fat little body off the ground.
            
            The bee, of course, flies anyway
            
            because bees don't care
            what humans think is impossible.
        """
        self.arr = []
        for i in range(20):
            newNum = random.randint(-100, 100)
            while newNum in self.arr:
                newNum = random.randint(-100, 100)
            self.arr.append(newNum)

        self.binaryTree = BinaryTree()
        self.binarySearchTree = BinarySearchTree()
        self.avlTree = AVLTree()
        
        for a in self.arr:
            self.binaryTree.insert(a)
            self.binarySearchTree.insert(a)
            self.avlTree.insert(a)
            
        self.segmentTree = SegmentTree(arr=self.arr)
        self.trie = Trie()
        for w in self.text.strip().replace('\n', '').split():
            self.trie.insert(w)
        
    # Binary Tree
    # Binary Search Tree
    # AVL Tree
        
    def test_search_success(self):
        # Binary Tree
        self.assertEqual(self.binaryTree.search(self.arr[0]).value, self.arr[0], "test_search_success, Binary Tree, arr[0]")
        self.assertEqual(self.binaryTree.search(self.arr[19]).value, self.arr[19], "test_search_success, Binary Tree, arr[19]")
        self.assertEqual(self.binaryTree.search(self.arr[10]).value, self.arr[10], "test_search_success, Binary Tree, arr[10]")
        
        # Binary Search Tree
        self.assertEqual(self.binarySearchTree.search(self.arr[0]).value, self.arr[0], "test_search_success, Binary Search Tree, arr[0]")
        self.assertEqual(self.binarySearchTree.search(self.arr[19]).value, self.arr[19], "test_search_success, Binary Search Tree, arr[19]")
        self.assertEqual(self.binarySearchTree.search(self.arr[10]).value, self.arr[10], "test_search_success, Binary Search Tree, arr[10]")
        
        # AVL Tree
        self.assertEqual(self.avlTree.search(self.arr[0]).value, self.arr[0], "test_search_success, AVL Tree, arr[0]")
        self.assertEqual(self.avlTree.search(self.arr[19]).value, self.arr[19], "test_search_success, AVL Tree, arr[19]")
        self.assertEqual(self.avlTree.search(self.arr[10]).value, self.arr[10], "test_search_success, AVL Tree, arr[10]")
        
    def test_search_failure(self):
        # Binary Tree
        self.assertEqual(self.binaryTree.search(300), None, "test_search_failure, Binary Tree, arr[0]")
        
        # Binary Search Tree
        self.assertEqual(self.binarySearchTree.search(300), None, "test_search_failure, Binary Search Tree, arr[0]")
        
        # AVL Tree
        self.assertEqual(self.avlTree.search(300), None, "test_search_failure, AVL Tree, arr[0]")
        
    def test_remove_success(self):
        countA = self.arr.count(self.arr[0])
        countB = self.arr.count(self.arr[19])
        countC = self.arr.count(self.arr[10])
        
        # Binary Tree
        # # Remove
        for i in range(countA):
            self.binaryTree.remove(self.arr[0])
        for i in range(countB):
            self.binaryTree.remove(self.arr[19])
        for i in range(countC):
            self.binaryTree.remove(self.arr[10])
        
        # # Search Failure
        self.assertEqual(self.binaryTree.search(self.arr[0]), None, f"test_search_success, Binary Tree, arr[0], {self.arr}")
        self.assertEqual(self.binaryTree.search(self.arr[19]), None, f"test_search_success, Binary Tree, arr[19], {self.arr}")
        self.assertEqual(self.binaryTree.search(self.arr[10]), None, f"test_search_success, Binary Tree, arr[10], {self.arr}")
        
        # Binary Search Tree
        # # Remove
        for i in range(countA):
            self.binarySearchTree.remove(self.arr[0])
        for i in range(countB):
            self.binarySearchTree.remove(self.arr[19])
        for i in range(countC):
            self.binarySearchTree.remove(self.arr[10])
        
        # # Search Failure
        self.assertEqual(self.binarySearchTree.search(self.arr[0]), None, f"test_search_success, Binary Search Tree, arr[0], {self.arr}")
        self.assertEqual(self.binarySearchTree.search(self.arr[19]), None, f"test_search_success, Binary Search Tree, arr[19], {self.arr}")
        self.assertEqual(self.binarySearchTree.search(self.arr[10]), None, f"test_search_success, Binary Search Tree, arr[10], {self.arr}")
        
        # AVL Tree
        # # Search Success
        
        # # Remove
        for i in range(countA):
            self.avlTree.remove(self.arr[0])
        for i in range(countB):
            self.avlTree.remove(self.arr[19])
        for i in range(countC):
            self.avlTree.remove(self.arr[10])
        
        # # Search Failure
        self.assertEqual(self.avlTree.search(self.arr[0]), None, f"test_search_success, AVL Tree, arr[0], {self.arr}")
        self.assertEqual(self.avlTree.search(self.arr[19]), None, f"test_search_success, AVL Tree, arr[19], {self.arr}")
        self.assertEqual(self.avlTree.search(self.arr[10]), None, f"test_search_success, AVL Tree, arr[10], {self.arr}")
        
    # Segment Tree
        
    def test_check_valid_sum(self):
        minRange = random.randint(0, len(self.arr) - 1)
        maxRange = random.randint(minRange, len(self.arr) - 1)
        self.assertEqual(self.segmentTree.getSum(minRange, maxRange), sum(self.arr[minRange: maxRange + 1]))
        
    def test_check_invalid_sum(self):
        minRange = -1
        maxRange = 5
        self.assertEqual(self.segmentTree.getSum(minRange, maxRange), None)
        
        minRange = -1
        maxRange = 100
        self.assertEqual(self.segmentTree.getSum(minRange, maxRange), None)
        
        minRange = 1
        maxRange = 100
        self.assertEqual(self.segmentTree.getSum(minRange, maxRange), None)
        
    # Trie
        
    def test_valid_words(self):
        self.assertEqual(self.trie.search("According"), True)
        self.assertEqual(self.trie.search("bee"), True)
        self.assertEqual(self.trie.search("impossible."), True)
        
    def test_invalid_words(self):
        self.assertEqual(self.trie.search("zxcasd"), False)
        self.assertEqual(self.trie.search("Bee"), False)
        self.assertEqual(self.trie.search("mpossible."), False)
        
        