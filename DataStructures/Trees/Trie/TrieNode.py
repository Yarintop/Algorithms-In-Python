class TrieNode:
    def __init__(self, char, isEndOfWord=False, alphabetLength=95) -> None: # 95 is from SPACE to ~ in ascii.
        self.char = char
        self.isEndOfWord = isEndOfWord
        self.children = [None] * alphabetLength # The reason we use a fixed array instead of using (if in) is that it's o(1) if we know the index.