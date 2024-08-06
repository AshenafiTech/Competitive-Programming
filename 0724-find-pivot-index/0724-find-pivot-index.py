class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        total = sum(nums)
        
        for i in range(len(nums)):
            total -= nums[i]
            if leftSum == total:
                return i
            else:
                leftSum+=nums[i]
                
        return -1