class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = float('inf')
        curr = 0
        for num in nums:
            curr+=num
            if curr < min_sum:
                min_sum = curr
                

        startValue = max(1, 1-min_sum)
        return startValue