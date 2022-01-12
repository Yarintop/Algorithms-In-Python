import functools
from Algorithms.MathematicalAlgorithms.GCD import GCD

class LCM:
    @staticmethod
    def LCM(a, b):
        """
            Find the Greatest Common Divisor
            Start with two numbers a>b≥0. You want to know two things:

            their greatest common divisor g,

            and how to represent g as a combination of a and b

            It's clear that you know both of these things in the easy special case when b=0.

            Suppose b>0. The divide a by b to get a quotient q and a remainder r strictly smaller than b:
            a=bq+r

            Now any number that divides both a and b also divides r, so divides both b and r. Also any number that divides both b and r also divides a, so divides both a and b. That means that the greatest common divisor of a and b is the same as the greatest common divisor of b and r, so (1) has the same answer g for both those pairs.

            Moreover, if you can write g as a combination of b and r then you can write it as a combination of a and b (substitute in (*)). That means if you can solve (2) for the pair (b,r) then you can solve it for the pair (a,b).

            Taken together, this argument shows that you can replace your problem for (a,b) by the same problem for the smaller pair (b,r). Since the problem can't keep getting smaller forever, eventually you will reach (z,0) and you're done.
            
            Source: https://math.stackexchange.com/questions/3379695/why-does-the-euclidean-algorithm-for-finding-LCM-work

        Args:
            a (int): The first number
            b (int): The second number

        Returns:
            int: The Greatest Common Divisor of a and b.
        """
        return int((a * b) / GCD.GCD(a, b))
    
    @staticmethod
    def LCMOfList(arr):
        return functools.reduce(lambda a, b: LCM.LCM(a, b), arr)
            
if __name__ == "__main__":
    print(LCM.LCM(18, 27)) # Should be 6.
    print(LCM.LCMOfList([12, 24, 27, 30, 36])) # Should be 6.
