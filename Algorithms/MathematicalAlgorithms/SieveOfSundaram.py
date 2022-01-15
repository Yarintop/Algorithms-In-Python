class SieveOfSundaram:
    @staticmethod
    def sieveOfSundaram(n):
        """
        sieve of Sundaram is a variant of the sieve of Eratosthenes, a simple deterministic algorithm for finding all the prime numbers up to a specified integer.

        If we start with integers from 1 to n, the final list contains only odd integers from 3 to 2n+1.
        From this final list, some odd integers have been excluded;
        we must show these are precisely the composite odd integers less than 2n + 2.

        Let q be an odd integer of the form 2k + 1. Then, q is excluded if and only if k is of the form i + j + 2ij, that is q = 2(i + j + 2ij) + 1. Then we have:

        q = 2(i + j + 2ij) + 1
        q = 2i + 2j + 4ij + 1
        q = (2i + 1)(2j + 1)
        So, an odd integer is excluded from the final list if and only if it has a factorization of the form (2i + 1)(2j + 1) — which is to say,
        if it has a non-trivial odd factor. Therefore the list must be composed of exactly the set of odd prime numbers less than or equal to 2n + 2.
        
        Source: https://en.wikipedia.org/wiki/Sieve_of_Sundaram
        
        Args:
            n (int): The maximum range
        """
        if n <= 1:
            return []
        k = (n - 2) // 2
        integersList = [True] * (k + 1)
        for i in range(1, k + 1):
            j = i
            while i + j + (2 * i * j) <= k:
                integersList[i + j + (2 * i * j)] = False
                j += 1
        primes = [2] + [(2*i) + 1 for i, x in enumerate(integersList) if x == True and i != 0]
        return primes
        
if __name__ == "__main__":
    print(SieveOfSundaram.sieveOfSundaram(1000))