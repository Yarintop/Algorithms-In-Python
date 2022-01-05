
class KMP:
    @staticmethod
    def kmp(text, pattern):
        """Searches a pattern in a text and returns the patterns' start indexes, using the KMP algorithm, if found.

        Args:
            text (String): text we're searching our pattern in.
            pattern (String): The pattern We're searching.

        Returns:
            list(Int): list of all indexes it found the pattern.
            
        Time Complexity:
            Worst-Case: O(n).
        """
        indexes = []
        lps = KMP.createLPSArray(pattern)
        i = j = 0
        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
            
            if j == len(pattern):
                indexes.append(i - j)
                j = lps[j - 1]
                
            elif i < len(text) and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return indexes
        
    @staticmethod
    def createLPSArray(pattern):
        """Creates an lps array (Longest prefix which is also a suffix) for each "State"

        Args:
            pattern (String): The pattern We're searching.

        Returns:
            list(Int): The lps array that tells us what state we're in after we found a mismatch, without the text again.
        """
        m = len(pattern)
        lps = [0] * m
        i = 1
        l = 0
        while i < m:
            if pattern[i] == pattern[l]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l != 0:
                    l = lps[l - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps
    
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
            
    pattern = ""
    
    print(KMP.kmp(text, pattern))
    