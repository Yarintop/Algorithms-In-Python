from DataStructures.Trees.Trie.TrieNode import TrieNode

ALPHABET_LENGTH = 95

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode(None, ALPHABET_LENGTH)
        
    def isEmpty(self):
        return self.root.children == [None] * ALPHABET_LENGTH
    
    def _isNodeEmpty(self, node):
        return node.children == [None] * ALPHABET_LENGTH

    def _translateCharToIndex(self, char):
        return ord(char) - ord(' ')

    def insert(self, string):
        currNode = self.root
        for s in string:
            try:
                index = self._translateCharToIndex(s)
                if currNode.children[index]:
                    currNode = currNode.children[index]
                else:
                    currNode.children[index] = TrieNode(s)
                    currNode = currNode.children[index]
            except:
                raise IndexError(
                    "Character is not valid, Please only choose characters from 32 (ASCII) to 126 (ASCII) Inclusive")

        currNode.isEndOfWord = True

    def search(self, string):
        currNode = self.root
        for s in string:
            try:
                index = self._translateCharToIndex(s)
                if currNode.children[index]:
                    currNode = currNode.children[index]
                else:
                    return False
            except:
                raise IndexError(
                    "Character is not valid, Please only choose characters from 32 (ASCII) to 126 (ASCII) Inclusive")

        return currNode.isEndOfWord
    
    def remove(self, string, currNode=None, depth = 0):
        if currNode == None:
            currNode = self.root
            
        if depth == len(string):
            if currNode.isEndOfWord:
                currNode.isEndOfWord = False
                
            if self._isNodeEmpty(currNode):
                return None
            
            return currNode
        
        index = self._translateCharToIndex(string[depth])
        currNode.children[index] = self.remove(string, currNode.children[index], depth + 1)
        
        if self._isNodeEmpty(currNode):
            return None
        
        return currNode


if __name__ == "__main__":
    trie = Trie()
    string = "The quick brown fox jumps over the lazy dog"
    for s in string.split():
        trie.insert(s)
        
    trie.insert('Th')
    trie.insert('jum')
    trie.insert('own')
    trie.insert('quic')
        
    print(f'"The" -> {trie.search("The")}')
    print(f'"brown" -> {trie.search("brown")}')
    print(f'"ve" -> {trie.search("ve")}')
    print(f'"la" -> {trie.search("la")}')
    print(f'"jum" -> {trie.search("jum")}')
    print(f'"th" -> {trie.search("th")}')
    print(f'"quic" -> {trie.search("quic")}')
    print(f'"Th" -> {trie.search("Th")}')
    print(f'"vcx" -> {trie.search("vcx")}')
    
    trie.remove('quic')
    print(f'"quic" -> {trie.search("quic")}')
    
    trie.remove('Th')
    print(f'"The" -> {trie.search("The")}')
    print(f'"Th" -> {trie.search("Th")}')

