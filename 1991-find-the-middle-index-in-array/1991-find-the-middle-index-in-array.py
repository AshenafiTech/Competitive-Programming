class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        curr = 0
        for i in range(len(nums)):
            total -= nums[i]
            
            if curr == total:
                return i
            else:
                curr+=nums[i]
                
        return -1