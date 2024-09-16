class Solution:
    def romanToInt(self, s: str) -> int:
        
        res = 0
        
        for i in range(len(s)-1, -1, -1):
                
            if s[i] == 'I':
                if (i < len(s)-1) and (s[i+1] == 'V' or s[i+1] == 'X'):
                    res-=1
                else:
                    res += 1
                
            if s[i] == 'V':
                res += 5
            
            if s[i] == 'X':
                if (i < len(s)-1) and ((s[i+1] == 'L' or s[i+1] == 'C')):
                    res-=10
                else:
                    res += 10
                
            if s[i] == 'L':
                res += 50
                
            if s[i] == 'C':
                if (i < len(s)-1) and (s[i+1] == 'D' or s[i+1] == 'M'):
                    res-=100
                else:
                    res += 100
                
            if s[i] == 'D':
                res += 500
                
            if s[i] == 'M':
                res += 1000
                
        return res
