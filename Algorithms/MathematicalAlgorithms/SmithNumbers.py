from Algorithms.MathematicalAlgorithms.PrimeFactors import PrimeFactors

class SmithNumbers:
    @staticmethod
    def smithNumbers(n):
        """
            Given a number n, the task is to find out whether this number is smith or not.
            A Smith Number is a composite number whose sum of digits is equal to the sum of digits in its prime factorization.
            
            Examples:
                Input  : n = 4
                Output : Yes
                Prime factorization = 2, 2  and 2 + 2 = 4
                Therefore, 4 is a smith number

                Input  : n = 6
                Output : No
                Prime factorization = 2, 3  and 2 + 3 is
                not 6. Therefore, 6 is not a smith number

                Input   : n = 666
                Output  : Yes
                Prime factorization = 2, 3, 3, 37 and
                2 + 3 + 3 + (3 + 7) = 6 + 6 + 6 = 18
                Therefore, 666 is a smith number

                Input   : n = 13
                Output  : No
                Prime factorization = 13 and 13 = 13,
                But 13 is not a smith number as it is not
                a composite number

        Args:
            n (int): The number we're checking.

        Returns:
            Bool: True if n is a smith number, else False.
        """
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
    