from HashFunctions import HashFunctions
from DataStructures.LinkedList.SinglyLinkedList import LinkedList

class ChainingHashig:
    def __init__(self, maxSize = 10000, hashFunction = HashFunctions.djb2a) -> None:
        self.maxSize = maxSize
        self.hash = [None] * maxSize
        self.hashFunction = hashFunction
    
    def insert(self, data):
        pos = self.hashFunction(data) % self.maxSize
        if self.hash[pos] == None:
            self.hash[pos] = LinkedList(data)
        else:
            self.hash[pos].push(data)
            
    def remove(self, data):
        pos = self.hashFunction(data) % self.maxSize
        if self.hash[pos] == None:
            raise ValueError(f"{data} is not in the HashMap.")
        else:
            try:
                self.hash[pos].remove(data)
            except ValueError:
                raise ValueError(f"{data} is not in the HashMap.")
            
    # def __getitem__(self, data):
    #     pos = self.hashFunction(data) % self.maxSize
        