class Solution:
    def reverseWords(self, s: str) -> str:

        # Remove leading and trailing spaces
        s = s.strip()
        s = ' '.join(s.split())
        s = list(s)
        self.reverse(s, 0, len(s)-1)

        start, end = 0, 0

        while end < len(s):
            if s[end] == ' ':
                self.reverse(s, start, end-1)
                start = end+1
            end+=1

        self.reverse(s, start, end-1)

        return ''.join(s)
    

    def reverse(self, s:list, start:int, end:int) -> None:
        while start < end:
            s[start], s[end] = s[end], s[start]
            start+=1
            end-=1




        

