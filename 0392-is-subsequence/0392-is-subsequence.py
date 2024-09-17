class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            if c in t:
                idx = t.index(c)+1
                t = t[idx:]
            else:
                return False

        return True
        