class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        m = int(math.sqrt(c))
        i = 0

        while i <= m:
            s = i**2 + m**2
            if s == c:
                return True
            elif s > c:
                m-=1
            else:
                i+=1
        return False