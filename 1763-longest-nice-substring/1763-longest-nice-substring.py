class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        longest = 0
        longest_nice = ""
        def is_nice(s):
            charSet = set(s)
            for ch in s:
                if ch.swapcase() not in charSet:
                    return False
            return True

        for l in range(len(s)):
            r = l+1
            while r!=len(s):
                sub_string = s[l:r+1]
                if is_nice(sub_string) and len(sub_string) > longest:
                    longest_nice = sub_string
                    longest = len(sub_string)
                    
                r+=1
        return longest_nice