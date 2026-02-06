class Solution:    
    def findUnion(self, a, b):
        # code here
        a = set(a)
        b = set(b)
        result = a.union(b)
        return result