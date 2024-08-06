class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        N = len(nums)
        curr = 0
        for index in range(N):
            curr += nums[index]

            if curr - nums[index] == total - curr:
                return index

        return -1