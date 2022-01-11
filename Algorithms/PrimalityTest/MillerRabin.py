import random
class MillerRabin:
    @staticmethod
    def millerRabin(n, k = 40):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n <= 1:
            return False
        
        def power(x, y, p):
            res = 1
            x = x % p
            
            while y > 0:
            
                if y % 2 == 1:
                    res = (res * x) % p
                    
                y = y // 2
                x = (x * x) % p
            return res
        
        def millerTest(d, n):
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