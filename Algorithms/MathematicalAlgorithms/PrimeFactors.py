
import math


class PrimeFactors:
    @staticmethod
    def primeFactors(n):
        factors = []
        while n % 2 == 0:
            n /= 2
            factors.append(2)
        for i in range(3, math.ceil(math.sqrt(n)), 2):
            while n % i == 0:
                n /= i
                factors.append(i)
        return factors
    
if __name__ == "__main__":
    n = 5940 # Factors are 2, 2, 3, 3, 3, 5, 11
    print(PrimeFactors.primeFactors(n))
    