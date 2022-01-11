# Sources: http://www.cse.yorku.ca/~oz/hash.html

from Algorithms.PrimalityTest.MillerRabin import MillerRabin

class HashFunctions:
    """
        Although Python can be faster with multiplications than bitwise,
        according to https://stackoverflow.com/questions/37053379/times-two-faster-than-bit-shift-for-python-3-x-integers,
        I've decided to write the algorithms using bitwise operations.
    """
    
    fnvConstants = {
        32: [16777619, 2166136261],
        64: [1099511628211, 14695981039346656037],
        128: [309485009821345068724781371, 144066263297769815596495629667062367629],
        256: [374144419156711147060143317175368453031918731002211, 100029257958052580907070968620625704837092796014241193945225284501741471925557],
        512: [35835915874844867368919076489095108449946327955754392558399825615420669938882575126094039892345713852759, 9659303129496669498009435400716310466090418745672637896108374329434462657994582932197716438449813051892206539805784495328239340083876191928701583869517785],
        1024: [5016456510113118655434598811035278955030765345404790744303017523831112055108147451509157692220295382716162651878526895249385292291816524375083746691371804094271873160484737966720260389217684476157468082573, 14197795064947621068722070641403218320880622795441933960878474914617582723252296732303717722150864096521202355549365628174669108571814760471015076148029755969804077320157692458563003215304957150157403644460363550505412711285966361610267868082893823963790439336411086884584107735010676915],
    }
    
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
    
    @staticmethod
    def djb2a(arr):
        """
            Another version of this djb2 (now favored by bernstein) uses xor: hash(i) = hash(i - 1) * 33 ^ str[i]
        """
        hash = 5381
        for e in arr:
            hash = ((hash << 5) + hash) ^ ord(e) # hash * 33 XOR e
                                            
        return hash
    
    @staticmethod
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
            
    @staticmethod
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
    
    @staticmethod
    def _fnv0(sizeInBits): # Deprecated, Only used to calculate FNV_offset_basis for fnv1.
        """
            https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function
        """
        hash = 0
        data = 'chongo <Landon Curt Noll> /\\../\\' # This is the string used to get the correct offset for fnv1.
        fnvPrime = HashFunctions._fnvPrimeCalculator(sizeInBits)
        for byte in data:
            byte = ord(byte)
            hash *= fnvPrime
            hash = hash ^ byte
            hash %= 2**(2**sizeInBits)
        
        return hash
        
    @staticmethod
    def _fnvPrimeCalculator(sizeInBits): # I won't use this function, I'll use the numbers in a hardcoded way.
        """
            Source: https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function
        """
        n = 2 ** sizeInBits
        t = (5 + n) // 12
        for b in range(1, 2 ** 8):
            bits = bin(b).count("1")
            if bits != 4 and bits != 5:
                continue
            p = (256 ** t) + (2 ** 8) + b
            if p % (2**40 - 2**24 - 1) > (2**24 + 2**8 + 2**7):
                if MillerRabin.millerRabin(p):
                    return p
    
    @staticmethod
    def fnv_1(data, sizeInBits=64):
        """
            Source: https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function
        """
        if sizeInBits not in HashFunctions.fnvConstants:
            raise ValueError("Please choose only 32, 64, 128, 256, 512 or 1024 as a bit size.")
        fnvPrime, hash = HashFunctions.fnvConstants[sizeInBits]
        for byte in data:
            byte = ord(byte)
            hash *= fnvPrime
            hash = hash ^ byte
            hash %= 2**(2**sizeInBits)
        
        return hash
    
    @staticmethod
    def fnv_1a(data, sizeInBits=64):
        """
            This algorithm is very similar FNV-1, we just changed the order of the multiplcation and XOR.
            The change in order leads to slightly better avalanche characteristics.
            Source: https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function
        """
        if sizeInBits not in HashFunctions.fnvConstants:
            raise ValueError("Please choose only 32, 64, 128, 256, 512 or 1024 as a bit size.")
        fnvPrime, hash = HashFunctions.fnvConstants[sizeInBits]
        for byte in data:
            byte = ord(byte)
            hash = hash ^ byte
            hash *= fnvPrime
            hash %= 2**(2**sizeInBits)
        
        return hash

