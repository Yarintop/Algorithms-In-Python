
class RabinKarp:
    @staticmethod
    def rabinKarp(text, pattern):
        """Searches a pattern in a text and returns the patterns' start indexes if found.
           Similar principle to the naive pattern, but instead of wasting time and checking string, we do a hash test before hand.

        Args:
            text (String): text we're searching our pattern in.
            pattern (String): The pattern We're searching.

        Returns:
            Int: The indexes where the substring matches. If the pattern is not in the text, returns -1.
            
        Time Complexity:
            Worst-Case: O(nm)
            Average and Best: O(n + m)
        """
        d = 256
        q = 601  # Random prime number.

        indexes = []

        n = len(text)
        m = len(pattern)

        i = t = p = 0
        h = 1

        for i in range(m - 1):
            h = (h*d) % q

        for i in range(m):
            t = (d*t + ord(text[i])) % q
            p = (d*p + ord(pattern[i])) % q

        for i in range(n - m + 1):
            if p == t:
                dirty = False
                for j in range(m):
                    if text[i + j] != pattern[j]:
                        dirty = True
                        break
                if not dirty:
                    indexes.append(i)
            if i < n - m:
                t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
                if t < 0:
                    t += q
                    
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

    print(RabinKarp.rabinKarp(text, pattern))
