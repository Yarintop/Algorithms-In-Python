import math
from Algorithms.PrimalityTest.MillerRabin import MillerRabin

class PrimeFactors:
    @staticmethod
    def primeFactors(n):
        """
            Get all prime factors of a number n. we first get all the 2's, after than the primes must be odds.
            so we start from 3 with increments of 2

        Args:
            n (int): The number we're trying to find its prime factors.

        Returns:
            list (int): All the prime factors of n.
        """
        factors = []
        while n % 2 == 0:
            n /= 2
            factors.append(2)
        for i in range(3, math.ceil(math.sqrt(n)), 2):
            while n % i == 0:
                n /= i
                factors.append(i)
        if MillerRabin.millerRabin(n):
            factors.append(int(n))
        return factors
    
if __name__ == "__main__":
    n = 5940 # Factors are 2, 2, 3, 3, 3, 5, 11
    print(PrimeFactors.primeFactors(n))
    