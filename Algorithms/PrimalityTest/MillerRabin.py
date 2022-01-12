import random
class MillerRabin:
    @staticmethod
    def millerRabin(n, k = 40):
        """
            The property is the following. For a given odd integer n > 2, let’s write n as 2s⋅d + 1 where s and d are positive integers and d is odd.
            Let’s consider an integer a, called a base, such that 0 < a < n.
            Then, n is said to be a strong probable prime to base a if one of these congruence relations holds:
            a^d ≡ 1(mod n).
            a^(2^r * d) ≡ -1(mod n) for some 0 ≤ r < s.
            
            The idea beneath this test is that when n is an odd prime, it passes the test because of two facts:
            1.  by Fermat's little theorem, a^(n-1) ≡ 1(mod n).
                (this property alone defines the weaker notion of probable prime to base a, on which the Fermat test is based);
            
            2.  the only square roots of 1 modulo n are 1 and −1.
            
            Hence, by contraposition, if n is not a strong probable prime to base a, then n is definitely composite,
            and a is called a witness for the compositeness of n (sometimes misleadingly called a strong witness).

            However, this property is not an exact characterization of prime numbers.
            If n is composite, it may nonetheless be a strong probable prime to base a, in which case it is called a strong pseudoprime,
            and a is a strong liar.

            Source: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

        Args:
            n (int): The number we're testing if prime
            k (int, optional): Number Of Tests. Defaults to 40.

        Returns:
            Bool: Returns False if n is not prime,
                  Returns True if n is PROBABLY prime, the margin of error is 1/(4^k). (k by default is 40 so this test is generally speaking pretty safe).
                  
        Time Complexity:
            Worst-Case: O(k(log^3(n))). note: The complexity can be reduced to O(k (log n)2 log2n log3n)-time by incorporating, say, 
                                              the Schonhage-Strassen algorithm for the fast multiplication of long integers.
        """
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n <= 1:
            return False
        
        def power(x, y, p):
            """
                This function is to help us power a number while using mod in between so it won't get too big.

            Args:
                x (int): The number we wan't to power.
                y (int): The power we would like to use.
                p (int): The mod number.

            Returns:
                int: (x ^ y) % p
            """
            res = 1
            x = x % p
            
            while y > 0:
            
                if y % 2 == 1:
                    res = (res * x) % p
                    
                y = y // 2
                x = (x * x) % p
            return res
        
        def millerTest(d, n):
            """
                We're taking a random number a and use our power function power(a, d, n) to create x.
                we then try to power x by itself mod n log(d) times. if x == 1 then our number is not prime.
                else, it could be prime and we keep checking until d != n-1

            Args:
                d (int): The power
                n (int): The mod number

            Returns:
                Bool: True if n is probably prime.
                      False if n is 100% not prime.
            """
            a = random.randint(2, n-2)
            x = power(a, d, n)
            if x == 1 or x == n - 1:
                return True
            
            while (d != n - 1):
                x = (x * x) % n
                d *= 2
                
                if x == 1:
                    return False
                if x == n - 1:
                    return True
            return False
        
        d = n - 1
        while d % 2 == 0:
            d = d // 2
            
        for i in range(k):
            if not millerTest(d, n):
                return False
            
        return True
        
if __name__ == "__main__":
    numbers = []
    with open('./Algorithms/PrimalityTest/primeNumbers.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            n = line.split()
            numbers += [int(x) for x in n]
    for n in numbers:
        if not MillerRabin.millerRabin(n):
            raise ValueError()