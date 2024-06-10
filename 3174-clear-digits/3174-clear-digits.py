class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        dig = set('0123456789')
        
        while True:
            boolean = False
            for i in s:
                if i in dig:
                    boolean = True
                    break
            if not boolean:
                break
            
            for i in range(len(s)):
                if s[i] in dig:
                    j = i
                    while j >= 0:
                        if s[j] not in dig:
                            s = s[:j] + s[i+1:]
                            break
                        j -= 1
                    else:
                        s = s[i+1:]
                    break
                
        return s