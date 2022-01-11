from HashFunctions import HashFunctions

class ChainingHashing:
    def __init__(self, maxSize = 10000, hashFunction = HashFunctions.djb2a) -> None:
        self.maxSize = maxSize
        self.hash = [[]] * maxSize
        self.hashFunction = hashFunction
    
    def insert(self, key, data):
        pos = self.hashFunction(key) % self.maxSize
        bucket = self.hash[pos]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                bucket[i] = (key, data)
                break
        else:
            bucket.append((key, data))
            
    def remove(self, key):
        pos = self.hashFunction(key) % self.maxSize
        bucket = self.hash[pos]
        if len(bucket) == 0:
            raise ValueError(f"{key} is not in the HashMap.")
        else:
            for i, kv in enumerate(bucket):
                k, v = kv
                if k == key:
                    del bucket[i]
                    break
            else:
                raise ValueError(f"{key} is not in HashMap.")
            
    def __getitem__(self, key):
        pos = self.hashFunction(key) % self.maxSize
        bucket = self.hash[pos]
        if len(bucket) == 0:
            return None
        else:
            for i, kv in enumerate(bucket):
                k, v = kv
                if k == key:
                    return v
            else:
                return None
            
    # def __getitem__(self, data):
    #     pos = self.hashFunction(data) % self.maxSize
        
if __name__ == "__main__":
    h = ChainingHashing()
    h.insert(1, 'a')
    h.insert(2, 'b')
    h.insert(3, 'c')
    h.insert(3, 'd')
    
    print(h[3])

    