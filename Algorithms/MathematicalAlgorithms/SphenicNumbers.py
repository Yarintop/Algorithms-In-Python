from Algorithms.MathematicalAlgorithms.PrimeFactors import PrimeFactors
from Algorithms.MathematicalAlgorithms.SieveOfSundaram import SieveOfSundaram

class SphenicNumbers:
    @staticmethod
    def sphenicNumber(n):
        """
            A Sphenic Number is a positive integer n which is product of exactly three distinct primes.
            Given a number n, determine whether it is a Sphenic Number or not.
            
            The idea is that if a number is a multiple of 3 prime numbers, it will have 6 divisors (8 if you count 1 and n itself).
            after we check if it has 6 divisors, we check if exactly three of them are unique primes.

        Args:
            n ([type]): [description]

        Returns:
            [type]: [description]
        """
        divisors = []
        smallerPrimes = SieveOfSundaram.sieveOfSundaram(n // 2)
        for i in range(2, n//2 + 1):
            if n % i == 0:
                divisors.append(i)
            if len(divisors) > 6:
                return False
            
        count = 0
        for d in divisors:
            if d in smallerPrimes:
                count += 1
        return count == 3
    
if __name__ == "__main__":
    arr = [12]
    for a in arr:
        print(SphenicNumbers.sphenicNumber(a))
    