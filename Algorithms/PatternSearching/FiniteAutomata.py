from unittest import result


class FiniteAutomata:
    @staticmethod
    def finiteAutomata(text, pattern):
        """Searches for patterns in string, when using a DFA (deterministic finite automata).

        Args:
            text (String): text we're searching our pattern in.
            pattern (String): The pattern We're searching.

        Returns:
            list(Int): list of all indexes it found the pattern.
        """
        indexes = []
        charDict = FiniteAutomata.getCharDict(text)
        tf = FiniteAutomata.computeTF(pattern, charDict)

        state = 0
        for i in range(len(text)):
            state = tf[state][charDict[text[i]]]
            if state == len(pattern):
                indexes.append(i - len(pattern) + 1)
        
        if indexes:
            return indexes
        return -1

    @staticmethod
    def computeTF(pattern, charDict):
        """Creates a TF table in order to know to what is the next state based on the next character.

        Args:
            pattern (String): The pattern We're searching.
            charDict (Dictionary): A dictionary that translates characters into their corresponding index.

        Returns:
            List (List (Integer)): Double array of integers that tells you what is the next state based on the current state and the current character.
        """
        tf = [[0 for i in range(len(charDict))] for j in range(len(pattern) + 1)]
        for state in range(len(pattern)):
            for char, v in charDict.items():
                tf[state][v] = FiniteAutomata.getNextState(pattern, state, char)

        return tf

    @staticmethod
    def getNextState(pattern, state, char):
        """Calculates the next state of the current 'Setup' (pattern, state, char).

        Args:
            pattern (String): The pattern We're searching.
            state (Integer): The current state we're in.
            char (String): The current Character.

        Returns:
            [type]: [description]
        """
        if state < len(pattern) and char == pattern[state]:
            return state + 1

        i = 0
        for ns in reversed(range(0, state)):
            if pattern[ns] == char:
                while i < ns:
                    if pattern[i] != pattern[state - ns + i]:
                        break
                    i += 1
                if i == ns - 1:
                    return ns
        return 0

    def getCharDict(text):
        """Convert every character in text to a unique number from 0 to len(text) so we could use a character as an array index.
           We can be more efficient if we know the alphabet before hand and therfore create a function beforehand
           (Such as, if we are only dealing with lower case characters, we could use ord(char) - 97).

        Args:
            text (String): The text we're taking our alphabet from.

        Returns:
            Dictionary: A dictionary that translates characters into their corresponding index.
            
        Time Complexity:
            Worst-Case: o(n)
        """
        l = len(set(text))
        return dict(zip(set(text), range(l)))


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

    pattern = "bee"

    print(FiniteAutomata.finiteAutomata(text, pattern))
