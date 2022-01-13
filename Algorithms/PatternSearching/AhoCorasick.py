from collections import defaultdict

class AhoCorasick:
    def __init__(self, words) -> None:
        self.maxStates = sum([len(word) for word in words])
        self.alphabetLength = 95
        self.out = [0] * (self.maxStates + 1)
        self.fail = [-1] * (self.maxStates + 1)
        self.nextState = [[-1] * self.alphabetLength for _ in range(self.maxStates + 1)]
        
        self.words = words
        self.numOfStates = self.__buildMatchingMachine()
        
    def __buildMatchingMachine(self):
        k = len(self.words)
        
        states = 1
        
        for i in range(k):
            word = self.words[i]
            currState = 0
            
            for char in word:
                c = ord(char) - ord(' ')
                
                if self.nextState[currState][c] == -1:
                    self.nextState[currState][c] = states
                    states += 1
                
                currState = self.nextState[currState][c]
                
            self.out[currState] |= (1 << i)
            
        q = []
        
        for c in range(self.alphabetLength):
            currNextState = self.nextState[0][c]
            
            if currNextState == -1:
                self.nextState[0][c] = 0
                
            elif currNextState != 0:
                self.fail[currNextState] = 0
                q.append(currNextState)
                
        while len(q) > 0:
            
            state = q.pop(0)
            
            for c in range(self.alphabetLength):
                if self.nextState[state][c] != -1:
                    failure = self.fail[state]
                    
                    while self.nextState[failure][c] == -1:
                        failure = self.fail[failure]
                        
                    failure = self.nextState[failure][c]
                    self.fail[self.nextState[state][c]] = failure
                    
                    self.out[self.nextState[state][c]] |= self.out[failure]
                    
                    q.append(self.nextState[state][c])
            
        return states
    
    def __findNextState(self, currState, nextChar):
        res = currState
        c = ord(nextChar) - ord(' ')
        
        while self.nextState[res][c] == -1:
            res = self.fail[res]
            
        return self.nextState[res][c]
    
    def searchWords(self, text):
        currState = 0
        
        res = defaultdict(list)
        
        for i in range(len(text)):
            currState = self.__findNextState(currState, text[i])
            
            if self.out[currState] == 0:
                continue
            
            for j in range(len(self.words)):
                if self.out[currState] & (1 << j) > 0:
                    word = self.words[j]
                    
                    res[word].append(i - len(word) + 1)
                    
        return res

if __name__ == "__main__":
    text = """According to all known laws
            of aviation,
            
            there is no way a bee
            should be able to fly.

            Its wings are too small to get
            its fat little body off the ground.
            
            The bee, of course, flies anyway
            
            because bees don't care
            what humans think is impossible."""
            
    words = ['Accord', 'bee', 'litte', 'cxzvxz', 'imposs']
    a = AhoCorasick(words)
    print(str(a.searchWords(text)))
    print()