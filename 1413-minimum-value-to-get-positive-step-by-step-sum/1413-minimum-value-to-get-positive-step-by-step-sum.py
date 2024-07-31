class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = []
        curr = 0
        for num in nums:
            curr+=num
            prefix.append(curr)

        m = min(prefix) 
        startValue = max(1, 1-m)
        return startValue