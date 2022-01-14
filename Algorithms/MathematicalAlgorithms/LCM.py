import functools
from Algorithms.MathematicalAlgorithms.GCD import GCD

class LCM:
    @staticmethod
    def LCM(a, b):
        """
            Find the Least Common Multiple. (Which is just (a X b)/GCD(a, b))

        Args:
            a (int): The first number
            b (int): The second number

        Returns:
            int: The Least Common Multiple of a and b.
        """
        return int((a * b) / GCD.GCD(a, b))
    
    @staticmethod
    def LCMOfList(arr):
        return functools.reduce(lambda a, b: LCM.LCM(a, b), arr)
            
if __name__ == "__main__":
    print(LCM.LCM(18, 27)) # Should be 6.
    print(LCM.LCMOfList([12, 24, 27, 30, 36])) # Should be 6.
