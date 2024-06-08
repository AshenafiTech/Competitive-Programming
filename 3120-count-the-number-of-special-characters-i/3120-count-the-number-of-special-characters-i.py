class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        lower = set()
        upper = set()

        for c in word:
            if c.isupper():
                upper.add(c.lower())
            elif c.islower():
                lower.add(c.lower())

        return len(lower & upper)

        