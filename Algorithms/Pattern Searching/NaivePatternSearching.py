
class NaivePatternSearching:
    @staticmethod
    def naivePatternSearching(text, pattern):
        """Searches a pattern in a text and returns the patterns' start indexes if found.

        Args:
            text (String): text we're searching our pattern in.
            pattern (String): The pattern We're searching.

        Returns:
            Int: The indexes where the substring matches. If the pattern is not in the text, returns -1.
            
        Time Complexity:
            Worst-Case: O(m*(n - m + 1)) -> m is the substring's length and n is our text's length.
        """
        indexes = []
        for i in range(len(text)):
            flag = True
            for j in range(len(pattern)):
                if text[i + j] != pattern[j]:
                    flag = False
                    break
            if flag:
                indexes.append(i)
        if len(indexes) == 0:
            return -1
        return indexes
    
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
    