import unittest
import random

from Algorithms.PatternSearching.NaivePatternSearching import NaivePatternSearching
from Algorithms.PatternSearching.KMP import KMP
from Algorithms.PatternSearching.RabinKarp import RabinKarp
from Algorithms.PatternSearching.FiniteAutomata import FiniteAutomata

class TestSearching(unittest.TestCase):
    
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.text = """According to all known laws
            of aviation,
            
            there is no way a bee
            should be able to fly.

            Its wings are too small to get
            its fat little body off the ground.
            
            The bee, of course, flies anyway
            
            because bees don't care
            what humans think is impossible."""
        
    # For Every Test, It checks if self.arr[The index the algorithms returns] is equal to self.arr[the index we gave].
    # The reason for this is in case there are duplicates, we don't want the assert to fail by checking the index.
    
    def test_first_string(self):
        pattern = "According"
        res = [0]
        self.assertEqual(NaivePatternSearching.naivePatternSearching(self.text, pattern), res, msg="test_first_string - Naive Pattern Searching")
        self.assertEqual(KMP.kmp(self.text, pattern), res, msg="test_first_string - KMP")
        self.assertEqual(RabinKarp.rabinKarp(self.text, pattern), res, msg="test_first_string - Rabin Karp")
        self.assertEqual(FiniteAutomata.finiteAutomata(self.text, pattern), res, msg="test_first_string - Finite Automata")
        
    def test_first_string_lower_case(self):
        pattern = "according"
        res = -1
        self.assertEqual(NaivePatternSearching.naivePatternSearching(self.text, pattern), res, msg="test_first_string - Naive Pattern Searching")
        self.assertEqual(KMP.kmp(self.text, pattern), res, msg="test_first_string - KMP")
        self.assertEqual(RabinKarp.rabinKarp(self.text, pattern), res, msg="test_first_string - Rabin Karp")
        self.assertEqual(FiniteAutomata.finiteAutomata(self.text, pattern), res, msg="test_first_string - Finite Automata")
    
    def test_first_character(self):
        pattern = "A"
        res = [0]
        self.assertEqual(NaivePatternSearching.naivePatternSearching(self.text, pattern), res, msg="test_first_value - Naive Pattern Searching")
        self.assertEqual(KMP.kmp(self.text, pattern), res, msg="test_first_value - KMP")
        self.assertEqual(RabinKarp.rabinKarp(self.text, pattern), res, msg="test_first_value - Rabin Karp")
        self.assertEqual(FiniteAutomata.finiteAutomata(self.text, pattern), res, msg="test_first_value - Finite Automata")
        
    def test_first_character_lower_case(self):
        pattern = "a"
        res = [13, 24, 43, 46, 91, 94, 122, 158, 168, 196, 278, 282, 313, 330, 348, 354]
        self.assertEqual(NaivePatternSearching.naivePatternSearching(self.text, pattern), res, msg="test_first_value - Naive Pattern Searching")
        self.assertEqual(KMP.kmp(self.text, pattern), res, msg="test_first_value - KMP")
        self.assertEqual(RabinKarp.rabinKarp(self.text, pattern), res, msg="test_first_value - Rabin Karp")
        self.assertEqual(FiniteAutomata.finiteAutomata(self.text, pattern), res, msg="test_first_value - Finite Automata")
    
    def test_last_string(self):
        pattern = "impossible."
        res = [367]
        self.assertEqual(NaivePatternSearching.naivePatternSearching(self.text, pattern), res, msg="test_first_value - Naive Pattern Searching")
        self.assertEqual(KMP.kmp(self.text, pattern), res, msg="test_first_value - KMP")
        self.assertEqual(RabinKarp.rabinKarp(self.text, pattern), res, msg="test_first_value - Rabin Karp")
        self.assertEqual(FiniteAutomata.finiteAutomata(self.text, pattern), res, msg="test_first_value - Finite Automata")
    
    def test_last_string_camal_case(self):
        pattern = "Impossible."
        res = -1
        self.assertEqual(NaivePatternSearching.naivePatternSearching(self.text, pattern), res, msg="test_first_value - Naive Pattern Searching")
        self.assertEqual(KMP.kmp(self.text, pattern), res, msg="test_first_value - KMP")
        self.assertEqual(RabinKarp.rabinKarp(self.text, pattern), res, msg="test_first_value - Rabin Karp")
        self.assertEqual(FiniteAutomata.finiteAutomata(self.text, pattern), res, msg="test_first_value - Finite Automata")
        
    def test_last_string_upper_case(self):
        pattern = "IMPOSSIBLE."
        res = -1
        self.assertEqual(NaivePatternSearching.naivePatternSearching(self.text, pattern), res, msg="test_first_value - Naive Pattern Searching")
        self.assertEqual(KMP.kmp(self.text, pattern), res, msg="test_first_value - KMP")
        self.assertEqual(RabinKarp.rabinKarp(self.text, pattern), res, msg="test_first_value - Rabin Karp")
        self.assertEqual(FiniteAutomata.finiteAutomata(self.text, pattern), res, msg="test_first_value - Finite Automata")
        
    def test_last_character(self):
        pattern = "."
        res = [133, 225, 377]
        self.assertEqual(NaivePatternSearching.naivePatternSearching(self.text, pattern), res, msg="test_first_value - Naive Pattern Searching")
        self.assertEqual(KMP.kmp(self.text, pattern), res, msg="test_first_value - KMP")
        self.assertEqual(RabinKarp.rabinKarp(self.text, pattern), res, msg="test_first_value - Rabin Karp")
        self.assertEqual(FiniteAutomata.finiteAutomata(self.text, pattern), res, msg="test_first_value - Finite Automata")
    
    def test_Bee(self):
        pattern = "Bee"
        res = -1
        self.assertEqual(NaivePatternSearching.naivePatternSearching(self.text, pattern), res, msg="test_first_value - Naive Pattern Searching")
        self.assertEqual(KMP.kmp(self.text, pattern), res, msg="test_first_value - KMP")
        self.assertEqual(RabinKarp.rabinKarp(self.text, pattern), res, msg="test_first_value - Rabin Karp")
        self.assertEqual(FiniteAutomata.finiteAutomata(self.text, pattern), res, msg="test_first_value - Finite Automata")
        
    def test_bee(self):
        pattern = "bee"
        res = [96, 256, 318]
        self.assertEqual(NaivePatternSearching.naivePatternSearching(self.text, pattern), res, msg="test_first_value - Naive Pattern Searching")
        self.assertEqual(KMP.kmp(self.text, pattern), res, msg="test_first_value - KMP")
        self.assertEqual(RabinKarp.rabinKarp(self.text, pattern), res, msg="test_first_value - Rabin Karp")
        self.assertEqual(FiniteAutomata.finiteAutomata(self.text, pattern), res, msg="test_first_value - Finite Automata")
        
    def test_BEE(self):
        pattern = "BEE"
        res = -1
        self.assertEqual(NaivePatternSearching.naivePatternSearching(self.text, pattern), res, msg="test_first_value - Naive Pattern Searching")
        self.assertEqual(KMP.kmp(self.text, pattern), res, msg="test_first_value - KMP")
        self.assertEqual(RabinKarp.rabinKarp(self.text, pattern), res, msg="test_first_value - Rabin Karp")
        self.assertEqual(FiniteAutomata.finiteAutomata(self.text, pattern), res, msg="test_first_value - Finite Automata")
    
    