class Solution:
    def isUgly(self, n: int) -> bool:
        limit = [1, 2, 3, 5]

        if n < 1:
            return False
        k = 2
        while k**2 <= n:
            if n % k == 0:
                if k not in limit:
                    return False
                n //= k
            else:
                k+=1
        if n > 1:
            if n not in limit:
                return False

        return True