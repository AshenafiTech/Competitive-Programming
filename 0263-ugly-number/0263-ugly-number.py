class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False
        def p_factors(n):
            k = 2
            factors = []

            while k**2 <= n:
                if n % k == 0:
                    factors.append(k)
                    n //= k
                else:
                    k+=1
            if n > 1:
                factors.append(n)
            return factors

        prime_factors = p_factors(n)
        limit = [2, 3, 5]

        for num in prime_factors:
            if num not in limit:
                return False
        return True