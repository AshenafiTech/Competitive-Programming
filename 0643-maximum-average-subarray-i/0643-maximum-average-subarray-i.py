class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0
        for i in range(k):
            curr+=nums[i]
        maxi = curr

        for i in range(k, len(nums)):
            curr+=nums[i]
            curr-=nums[i-k]
            maxi = max(curr, maxi)

        return maxi/k