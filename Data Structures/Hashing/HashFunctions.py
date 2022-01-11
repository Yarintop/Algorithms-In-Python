# Sources: http://www.cse.yorku.ca/~oz/hash.html

class HashFunctions:
    """
        Although Python can be faster with multiplications than bitwise,
        according to https://stackoverflow.com/questions/37053379/times-two-faster-than-bit-shift-for-python-3-x-integers,
        I've decided to write the algorithms using bitwise operations.
    """
    @staticmethod
    def djb2(arr):
        """
            DJBX33A (Daniel J. Bernstein, Times 33 with Addition)

            This is Daniel J. Bernstein's popular `times 33' hash function as
            posted by him years ago on comp.lang.c. It basically uses a function
            like ``hash(i) = hash(i-1) * 33 + str[i]''. This is one of the best
            known hash functions for strings. Because it is both computed very
            fast and distributes very well.

            The magic of number 33, i.e. why it works better than many other
            constants, prime or not, has never been adequately explained by
            anyone. So I try an explanation: if one experimentally tests all
            multipliers between 1 and 256 (as RSE did now) one detects that even
            numbers are not useable at all. The remaining 128 odd numbers
            (except for the number 1) work more or less all equally well. They
            all distribute in an acceptable way and this way fill a hash table
            with an average percent of approx. 86%.

            If one compares the Chi^2 values of the variants, the number 33 not
            even has the best value. But the number 33 and a few other equally
            good numbers like 17, 31, 63, 127 and 129 have nevertheless a great
            advantage to the remaining numbers in the large set of possible
            multipliers: their multiply operation can be replaced by a faster
            operation based on just one shift plus either a single addition
            or subtraction operation. And because a hash function has to both
            distribute good _and_ has to be very fast to compute, those few
            numbers should be preferred and seems to be the reason why Daniel J.
            Bernstein also preferred it.
            
            DJB: "Practically any good multiplier works.
            I think you're worrying about the fact that 31c + d doesn't cover any reasonable range of hash values if c and d are between 0 and 255.
            That's why, when I discovered the 33 hash function and started using it in my compressors, I started with a hash value of 5381.
            I think you'll find that this does just as well as a 261 multiplier."
        """
        hash = 5381
        for e in arr:
            hash = ((hash << 5) + hash) + ord(e) # hash * 33 + e
                                            
        return hash
    
    def djb2(arr):
        """
            Another version of this djb2 (now favored by bernstein) uses xor: hash(i) = hash(i - 1) * 33 ^ str[i]
        """
        hash = 5381
        for e in arr:
            hash = ((hash << 5) + hash) ^ ord(e) # hash * 33 + e
                                            
        return hash
    
    def sdbm(arr):
        """
            this algorithm was created for sdbm (a public-domain reimplementation of ndbm) database library.
            it was found to do well in scrambling bits, causing better distribution of the keys and fewer splits.
            it also happens to be a good general hashing function with good distribution.
            the actual function is hash(i) = hash(i - 1) * 65599 + str[i]; what is included below is the faster version used in gawk.
            the magic constant 65599 was picked out of thin air while experimenting with different constants, and turns out to be a prime
            this is one of the algorithms used in berkeley db (see sleepycat) and elsewhere.
        """
        hash = 0
        for e in arr:
            hash = (hash << 6) + (hash << 16) - hash + ord(e) # hash * 65599 + e
            
        return hash
            
    def loseLose(arr):
        """
            This hash function appeared in K&R (1st ed) but at least the reader was warned:
            "This is not the best possible algorithm, but it has the merit of extreme simplicity."
            This is an understatement; It is a terrible hashing algorithm, and it could have been much better without sacrificing its "extreme simplicity."
            Many C programmers use this function without actually testing it, or checking something like Knuth's Sorting and Searching, so it stuck.
            It is now found mixed with otherwise respectable code
        """
        hash = 0
        for e in arr:
            hash += ord(e)
            
        return hash
    
    # def fnvPrimeCalculator(sizeInBits):
    #     for s in range(4, 12):
    #         n = 2 ** s
    #         t = (5 + n) // 12
            
    
    # def fnv1_32
    
    

if __name__ == "__main__":
    HashFunctions.djb2('asd')