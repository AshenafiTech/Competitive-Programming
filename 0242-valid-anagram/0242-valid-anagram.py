class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        is_anagram = True
        if (len(s) != len(t)):
            return False

        for i in range(len(s)):
            if s[i] not in t:
                is_anagram = False
                break
            idx = t.index(s[i])
            t = t[0:idx] + t[idx+1:]

        return is_anagram
        