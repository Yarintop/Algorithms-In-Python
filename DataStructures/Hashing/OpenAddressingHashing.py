from HashFunctions import HashFunctions
from enum import Enum

class ProbingMethod(Enum):
    LINEAR_PROBING = 0
    QUADRATIC_PROBING = 1
    DOUBLE_HASHING = 2
    
class Deleted:
    pass

class OpenAddressingHashing:
    def __init__(self, maxSize=10000, probingMethod=ProbingMethod.LINEAR_PROBING, hashFunction1=HashFunctions.djb2a, hashFunction2=HashFunctions.djb2a) -> None:
        self.maxSize = maxSize
        self.hash = [None] * maxSize
        self.hashFunction1 = hashFunction1
        self.hashFunction2 = hashFunction2
        
        if probingMethod == 0:
            self.probingMethod = self._linearProbing
        elif probingMethod == 1:
            self.probingMethod = self._quadraticProbing
        else:
            self.probingMethod = self._doubleHashing
    
    def insert(self, key, data):
        pos = self.probingMethod(key, 0)
        i = 1
        while self.hash[pos] != None and not isinstance(self.hash[pos], Deleted):
            if self.hash[pos][0] == key:
                break
            if i >= self.maxSize * 2:
                raise Exception(f"Could not insert ({key}, {data}) To the HashMap (looped {self.maxSize * 2} times to find an open slot.")
            pos = self.probingMethod(key, i)
            i += 1
        self.hash[pos] = (key, data)
            
    def remove(self, key):
        pos = self.probingMethod(key, 0)
        i = 1
        while self.hash[pos] != None and not isinstance(self.hash[pos], Deleted):
            if self.hash[pos][0] == key:
                break
            if i >= self.maxSize * 2:
                raise ValueError(f"Could not find the key: ({key}) in the HashMap (looped {self.maxSize * 2} times to find an open slot.")
            pos = self.probingMethod(key, i)
            i += 1
        self.hash[pos] = Deleted()
            
    def __getitem__(self, key):
        pos = self.probingMethod(key, 0)
        i = 1
        while self.hash[pos] != None and not isinstance(self.hash[pos], Deleted):
            if self.hash[pos][0] == key:
                break
            if i >= self.maxSize * 2:
                raise ValueError(f"Could not find the key: ({key}) in the HashMap (looped {self.maxSize * 2} times to find an open slot.")
            pos = self.probingMethod(key, i)
            i += 1
        return self.hash[pos]
            
        
    def _linearProbing(self, key, p):
        return (self.hashFunction1(key) + p) % self.maxSize

    def _quadraticProbing(self, key, p):
        return (self.hashFunction1(key) + (p * 2)) % self.maxSize
    
    def _doubleHashing(self, key, p):
        return (self.hashFunction1(key) + (p * self.hashFunction2(key))) % self.maxSize
        
if __name__ == "__main__":
    h = OpenAddressingHashing()
    h.insert(1, 'a')
    h.insert(2, 'b')
    h.insert(3, 'c')
    h.insert(3, 'd')
    
    print(h[3])
    