class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        # base case
        if n == 1: return True
        if n < 1: return False

        # function calling itself with change in state
        return self.isPowerOfFour(n/4)