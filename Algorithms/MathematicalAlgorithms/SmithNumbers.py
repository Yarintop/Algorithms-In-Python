from Algorithms.MathematicalAlgorithms.PrimeFactors import PrimeFactors

class SmithNumbers:
    @staticmethod
    def smithNumbers(n):
        primeFactors = PrimeFactors.primeFactors(n)
        
        if not primeFactors or primeFactors[0] == n:
            return False

        primeFactorsDigits = [list(str(digit)) for digit in primeFactors]
        primeFactorsDigits = [int(val) for sublist in primeFactorsDigits for val in sublist]
        
        return sum(primeFactorsDigits) == sum([int(x) for x in str(n)])
    
if __name__ == "__main__":
    print(SmithNumbers.smithNumbers(4)) # True, 2 + 2 = 4
    print(SmithNumbers.smithNumbers(6)) # False, 2 + 3 != 6
    print(SmithNumbers.smithNumbers(666)) # True, 2 + 3 + 3 + 3 + 7 = 6 + 6 + 6 = 18
    print(SmithNumbers.smithNumbers(13)) # False, although 13 = 13, a smith number must be a composite number and can't be prime.
    