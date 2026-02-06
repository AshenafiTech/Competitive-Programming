class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        if len(a) != len(b):
            return False
            
        freq = {}
        
        for x in a:
            freq[x] = freq.get(x, 0) + 1
            
        for y in b:
            if y not in freq:
                return False
            freq[y] -= 1
            
            if freq[y] < 0:
                return False
                
                
        return True