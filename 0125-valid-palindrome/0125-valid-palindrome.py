class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(filter(str.isalnum, s.lower()))
        l =0
        r = len(s)-1
        
        while l<r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True