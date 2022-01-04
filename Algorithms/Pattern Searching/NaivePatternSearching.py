
class NaivePatternSearching:
    @staticmethod
    def naivePatternSearching(text, pattern):
        """Searches a pattern in a text and returns it's start index if found.

        Args:
            text (String): text we're searching our pattern in.
            pattern (String): The pattern We're searching.

        Returns:
            Int: The index where the substring matches. If the pattern is not in the text, returns -1.
            
        Time Complexity:
            Worst-Case: O(m*(n - m + 1)) -> m is the substring's length and n is our text's length.
        """
        for i in range(len(text)):
            flag = True
            for j in range(len(pattern)):
                if text[i + j] != pattern[j]:
                    flag = False
                    break
            if flag:
                return i
        return -1
    
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
    
    print(NaivePatternSearching.naivePatternSearching(text, pattern))
    