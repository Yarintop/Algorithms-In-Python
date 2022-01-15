from DataStructures.Trees.BinaryTree.BinaryTreeNode import BinaryTreeNode
from DataStructures.Queues.PriorityQueue.PriorityQueue import PriorityQueue

class HuffmanCoding:
    """
        Huffman coding is a lossless data compression algorithm. The idea is to assign variable-length codes to input characters,
        lengths of the assigned codes are based on the frequencies of corresponding characters.
        The most frequent character gets the smallest code and the least frequent character gets the largest code.
        The variable-length codes assigned to input characters are Prefix Codes,
        means the codes (bit sequences) are assigned in such a way that the code assigned to one character is not the prefix of code
        assigned to any other character. This is how Huffman Coding makes sure that there is no ambiguity when decoding the generated bitstream.
    """
    def __init__(self, text):
        self.currByte = 0x0
        self.currByteIndex = 7
        self.buffer = []
        
        
        if len(text) == 0:
            self.root = None
            return
        
        pq = PriorityQueue()
        for t in set(text):
            pq.push(BinaryTreeNode((text.count(t), t)))
        
        while len(pq) > 1:
            nodeA = pq.get()
            nodeB = pq.get()
            self.root = BinaryTreeNode((nodeA.value[0] + nodeB.value[0], ), nodeA, nodeB)
            pq.push(self.root)
            
        self.currNode = self.root
        self.decodedMessage = ""
            
    def _incrementByte(self, right):
        if self.currByteIndex < 0:
            self.currByteIndex = 7
            self.buffer.append(self.currByte)
            self.currByte = 0b0
            
        if right:
            self.currByte |= 1 << self.currByteIndex
        self.currByteIndex -= 1
            
            
    def _encodeChar(self, char, node=None, firstRun=True):
        if node == None:
            node = self.root
            
        res = []
            
        if node.left and node.right:
            leftEncode = self._encodeChar(char, node.left, False)
            if leftEncode:
                if not firstRun:
                    if leftEncode == True:
                        return [0]
                    return [0] + leftEncode
                res = [0] + leftEncode
            else:
                rightEncode = self._encodeChar(char, node.right, False)
                if rightEncode:
                    if not firstRun:
                        if rightEncode == True:
                            return [1]
                        return [1] + rightEncode
                    res = [1] + rightEncode
            
            if firstRun:
                for r in res:
                    self._incrementByte(int(r))
        else:
            if node.value[1] == char:
                return True
            return None
        
    def _decodeChar(self, nextBit):
        try:
            if nextBit == "0":
                self.currNode = self.currNode.left
            else:
                self.currNode = self.currNode.right
            
            if not self.currNode.left and not self.currNode.right:
                self.decodedMessage += self.currNode.value[1]
                self.currNode = self.root
        except:
            raise IndexError("Encoded char doesn't exist in the huffman tree.")
            
    def encodeMessage(self, text):
        with open('./Algorithms/Compression/HuffmanEncodedMessage.txt', 'wb') as f:
            for char in text:
                self._encodeChar(char)
                while len(self.buffer) > 0:
                    b = self.buffer.pop(0)
                    f.write(b.to_bytes(1, 'big'))
            if self.currByte != 0b0:
                f.write(self.currByte.to_bytes(1, 'big'))
                self.currByte = 0b0
                
    def decodeMessage(self):
        try:
            self.currNode = self.root
            self.decodedMessage = ""
            with open('./Algorithms/Compression/HuffmanEncodedMessage.txt', 'rb') as f:
                byte = f.read(1)
                while byte != b'':
                    binaryNumber = bin(int.from_bytes(byte, 'big'))[2:]
                    for i in range(8 - len(binaryNumber)):
                        self._decodeChar("0")
                    for c in bin(int.from_bytes(byte, 'big'))[2:]:
                        self._decodeChar(c)
                    byte = f.read(1)
            print(self.decodedMessage)
        except IndexError:
            print(self.decodedMessage)
        
if __name__ == "__main__":
    huffman = HuffmanCoding("ttgagatcggctcctgttaacctgttagacttgtaaatattgacatcctgggaacggtcttccttccttctccgcgcgctagccctggcccaacactgcgggggaaacccgggttttctttacagaccaggcacttctttggcgaggtagttcttaatcatgtaacttgcgactggtggccgtaccaactaaacggcgcgttgcatccacgaagggggttaccctgcggctacctctgcataggcacgatagcttaacccgctcaaacttggtcgcagtcatgtcccactagctaccacccgggttatgcttaacacttcaaaatgggttactccagtcttccctattcatcagttcataaagcgagtgttcgagtcctcgcgaccccatgatccttgctgcatactagccataagactactaattctgcgggtttgcctctgttgtattgtcgctattagccggacaagtaaccagagcaagaagccacacagtggctggtatcgacgcacaaaagtcctcttatcagcagtagcatacagacgtccgctatgcgtttgaacaggtggagtggtaggtgatgtgactcttctcttacgccggacttcattagcggcaggacggacaccctgttgagagatctcgacattcttatcaccagcctggaaccgagcattcactgatccaatactggccgtacgtacccacactacgttcacatatcaataggctcgctggacaacacgggacacgctattgaagctgtgatgagaggctcttattgccgcggcgggctggctctaacacactcgcttgcgtcgaatggggcgcctagtggacgctatgcgactcaactaccaactaaccactaactatagggtaggctttgaagtgctgctggcttcgtttgtgctagccttttggatagatattacggcttcaatccatagcgtaccaagaaacaatgtttgtggctccgcgcacctgatgtcaatgcaac")   
    huffman.encodeMessage("ttgagatcggctcctgttaacctgttagacttgtaaatattgacatcctgggaacggtcttccttccttctccgcgcgctagccctggcccaacactgcgggggaaacccgggttttctttacagaccaggcacttctttggcgaggtagttcttaatcatgtaacttgcgactggtggccgtaccaactaaacggcgcgttgcatccacgaagggggttaccctgcggctacctctgcataggcacgatagcttaacccgctcaaacttggtcgcagtcatgtcccactagctaccacccgggttatgcttaacacttcaaaatgggttactccagtcttccctattcatcagttcataaagcgagtgttcgagtcctcgcgaccccatgatccttgctgcatactagccataagactactaattctgcgggtttgcctctgttgtattgtcgctattagccggacaagtaaccagagcaagaagccacacagtggctggtatcgacgcacaaaagtcctcttatcagcagtagcatacagacgtccgctatgcgtttgaacaggtggagtggtaggtgatgtgactcttctcttacgccggacttcattagcggcaggacggacaccctgttgagagatctcgacattcttatcaccagcctggaaccgagcattcactgatccaatactggccgtacgtacccacactacgttcacatatcaataggctcgctggacaacacgggacacgctattgaagctgtgatgagaggctcttattgccgcggcgggctggctctaacacactcgcttgcgtcgaatggggcgcctagtggacgctatgcgactcaactaccaactaaccactaactatagggtaggctttgaagtgctgctggcttcgtttgtgctagccttttggatagatattacggcttcaatccatagcgtaccaagaaacaatgtttgtggctccgcgcacctgatgtcaatgcaac")
    huffman.decodeMessage()
    